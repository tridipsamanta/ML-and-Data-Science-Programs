import tensorflow as tf
import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw
import struct
from array import array
import os
import time

# ---------- LOAD MNIST LOCALLY ----------
def load_mnist(images_path, labels_path):
    with open(labels_path, 'rb') as lb:
        magic, size = struct.unpack(">II", lb.read(8))
        labels = array("B", lb.read())

    with open(images_path, 'rb') as img:
        magic, size, rows, cols = struct.unpack(">IIII", img.read(16))
        image_data = array("B", img.read())

    images = []
    for i in range(size):
        img = np.array(image_data[i*rows*cols:(i+1)*rows*cols])
        images.append(img.reshape(28, 28) / 255.0)

    return np.array(images), np.array(labels)

BASE = os.path.dirname(os.path.abspath(__file__))

x_train, y_train = load_mnist(
    os.path.join(BASE, "train-images.idx3-ubyte"),
    os.path.join(BASE, "train-labels.idx1-ubyte")
)

# ---------- BUILD CNN ----------
model = tf.keras.Sequential([
    tf.keras.layers.Reshape((28, 28, 1), input_shape=(28, 28)),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("Training model (one time)...")
model.fit(x_train, y_train, epochs=3, verbose=1)

# ---------- GUI ----------
class DrawApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Live Digit Recognition")

        self.canvas = tk.Canvas(self.root, width=280, height=280, bg="black")
        self.canvas.pack()

        self.pred_label = tk.Label(self.root, text="Prediction:", font=("Arial", 18))
        self.pred_label.pack(pady=10)

        tk.Button(self.root, text="Clear", command=self.clear).pack()

        self.image = Image.new("L", (280, 280), "black")
        self.draw = ImageDraw.Draw(self.image)

        self.last_time = time.time()
        self.canvas.bind("<B1-Motion>", self.paint)

        self.root.mainloop()

    def paint(self, event):
        r = 8
        x, y = event.x, event.y
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="white", outline="white")
        self.draw.ellipse((x-r, y-r, x+r, y+r), fill="white")

        if time.time() - self.last_time > 0.2:
            self.predict()
            self.last_time = time.time()

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle((0, 0, 280, 280), fill="black")
        self.pred_label.config(text="Prediction:")

    def predict(self):
        img = self.image.resize((28, 28))
        img = np.array(img) / 255.0
        img = img.reshape(1, 28, 28)

        pred = np.argmax(model.predict(img, verbose=0))
        self.pred_label.config(text=f"Prediction: {pred}")

# ---------- RUN ----------
DrawApp()
