# ✍️ Live Handwritten Digit Recognition (Offline)

A **real-time handwritten digit recognition application** built using **Python, TensorFlow, and Tkinter**.  
The app allows users to **draw digits with a mouse** and see **live predictions directly inside the same window**.

---

## 🖼️ Demo

<p align="center">
  <img src="images/live_digit_recognition.png" width="400">
</p>

---

## 🚀 Features

- 🖊️ Draw digits in a black canvas
- 🔄 **Live prediction while drawing**
- 🧠 CNN-based digit classifier trained on MNIST
- 🪟 Single popup window (no extra figures)
- 🌐 Works completely **offline**
- 🔐 Avoids TensorFlow SSL issues
- 🧹 Clear button to reset drawing

---

## 🧠 Model Details

- Dataset: **MNIST (locally loaded)**
- Model: **Convolutional Neural Network (CNN)**
- Layers:
  - Conv2D → ReLU → MaxPooling
  - Conv2D → ReLU → MaxPooling
  - Dense → Softmax
- Optimizer: Adam  
- Loss: Sparse Categorical Crossentropy

---
## 📦 Requirements

```bash
pip install tensorflow pillow numpy

▶️ How to Run
python digit_draw_live_local.py
