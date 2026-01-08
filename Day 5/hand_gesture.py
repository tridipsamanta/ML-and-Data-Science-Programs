import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

def count_fingers(hand_landmarks, handedness_label: str) -> int:
    """
    Count raised fingers for a single hand using landmark positions.

    Logic:
    - Thumb: compare tip (4) to IP joint (3) along x-axis; left/right hands are mirrored.
      Right hand: thumb is raised if tip.x < ip.x (tip to the left).
      Left hand:  thumb is raised if tip.x > ip.x (tip to the right).
    - Other fingers (Index/Middle/Ring/Pinky): tip above PIP along y-axis.
      A finger is raised if tip.y < pip.y (remember: y grows downward in image space).
    """
    lm = hand_landmarks.landmark

    count = 0
    # Thumb
    thumb_tip_x = lm[4].x
    thumb_ip_x = lm[3].x
    if handedness_label == "Right":
        if thumb_tip_x < thumb_ip_x:
            count += 1
    else:  # "Left"
        if thumb_tip_x > thumb_ip_x:
            count += 1

    # Index, Middle, Ring, Pinky
    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]
    for tip_idx, pip_idx in zip(finger_tips, finger_pips):
        tip_y = lm[tip_idx].y
        pip_y = lm[pip_idx].y
        if tip_y < pip_y:
            count += 1

    return count

def open_camera() -> cv2.VideoCapture:
    """
    Try opening the camera with macOS AVFoundation backend first, then fallback.
    Returns an opened VideoCapture or None-like if failed.
    """
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
    if not cap.isOpened():
        cap.release()
        cap = cv2.VideoCapture(0)
    return cap

def main():
    # Safety: try to open camera
    cap = open_camera()
    if not cap or not cap.isOpened():
        print(
            "Error: Unable to access the camera. On macOS, ensure the app (Terminal/VS Code) has camera permissions under System Settings → Privacy & Security → Camera."
        )
        return

    # MediaPipe Hands configuration (classic solutions API)
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        model_complexity=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    )

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("Warning: Failed to read from camera. Exiting.")
                break

            # Flip for natural selfie-view; MediaPipe expects RGB
            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(rgb)

            total_count = 0

            if results.multi_hand_landmarks:
                # handedness info aligns with multi_hand_landmarks order
                handedness_list = (
                    results.multi_handedness if results.multi_handedness else []
                )

                for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
                    # Determine Left/Right label safely
                    label = "Right"
                    if i < len(handedness_list):
                        try:
                            label = handedness_list[i].classification[0].label
                        except Exception:
                            label = "Right"

                    # Draw landmarks
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_styles.get_default_hand_landmarks_style(),
                        mp_styles.get_default_hand_connections_style(),
                    )

                    # Count fingers for this hand
                    total_count += count_fingers(hand_landmarks, label)

            # Overlay total finger count
            cv2.rectangle(frame, (10, 10), (200, 70), (0, 0, 0), -1)
            cv2.putText(
                frame,
                f"Fingers: {total_count}",
                (20, 55),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (255, 255, 255),
                2,
            )

            cv2.imshow("Hand Gesture / Finger Counting", frame)

            # Exit on ESC
            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                break
    finally:
        # Clean shutdown
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2, detectionCon=0.8)

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img)

    totalFingers = 0

    if hands:
        for hand in hands:
            fingers = detector.fingersUp(hand)
            totalFingers += fingers.count(1)

    cv2.putText(img, f'Fingers: {totalFingers}', (30, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Counter", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
