# ✍️ Live Handwritten Digit Recognition (Offline, GUI)

This project is a **live handwritten digit recognition system** built using **Python, TensorFlow, and Tkinter**.

It allows you to:
- Draw digits using your mouse
- See the **prediction continuously updated in real time**
- Run **completely offline** (no internet, no SSL issues)
- Use your **locally downloaded MNIST dataset**

---

## 🚀 Features

- 🖊️ Draw digits in a black canvas window
- 🔄 **Live prediction updates while drawing**
- 🧠 Convolutional Neural Network (CNN) trained on MNIST
- 🪟 Single popup window (no extra Matplotlib windows)
- 🌐 No internet required
- 🔐 Avoids TensorFlow SSL certificate errors
- 🧹 Clear button to reset drawing

---

## 🧠 Model Used

- **Convolutional Neural Network (CNN)**
- Architecture:
  - Conv2D + ReLU
  - MaxPooling
  - Conv2D + ReLU
  - MaxPooling
  - Dense layers
- Trained on the **MNIST handwritten digits dataset**
- Optimizer: Adam
- Loss: Sparse Categorical Crossentropy

---

## 📁 Project Structure

mnist/
├── Digit_analyzer.py # (optional older script)
├── digit_draw_live_local.py # Main application (run this)
├── train-images.idx3-ubyte
├── train-labels.idx1-ubyte
├── t10k-images.idx3-ubyte
├── t10k-labels.idx1-ubyte
└── README.md



⚠️ **Important**:  
The MNIST files must be in the **same folder** as the Python script.

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install tensorflow pillow numpy
