import tkinter as tk
import numpy as np
import struct
from array import array
import os
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

#  ---------------- MNIST LOADER ----------------
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

# ---------------- LOAD DATA ----------------
BASE = os.path.dirname(os.path.abspath(__file__))

x_train, y_train = load_mnist(
    os.path.join(BASE, "train-images.idx3-ubyte"),
    os.path.join(BASE, "train-labels.idx1-ubyte")
)

# ---------------- SIMPLE CLASSIFIER ----------------
x_train_flat = x_train.reshape(len(x_train), -1)

digit_means = np.zeros((10, 784))
for d in range(10):
    digit_means[d] = x_train_flat[y_train == d].mean(axis=0)

def predict_digit(image):
    image = image.flatten()
    return np.argmin(np.linalg.norm(digit_means - image, axis=1))

# ---------------- GUI ----------------
class DrawApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Draw a Digit")

        self.canvas = tk.Canvas(self.root, width=280, height=280, bg="black")
        self.canvas.pack()

        self.image = Image.new("L", (280, 280), "black")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)

        tk.Button(self.root, text="Predict", command=self.predict).pack(side="left")
        tk.Button(self.root, text="Clear", command=self.clear).pack(side="right")

        self.root.mainloop()

    def paint(self, event):
        x, y = event.x, event.y
        r = 10
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="white", outline="white")
        self.draw.ellipse((x-r, y-r, x+r, y+r), fill="white")

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle((0, 0, 280, 280), fill="black")

    def predict(self):
        img = self.image.resize((28, 28))
        img = np.array(img) / 255.0
        pred = predict_digit(img)

        plt.imshow(img, cmap="gray")
        plt.title(f"Predicted Digit: {pred}")
        plt.axis("off")
        plt.show()

# ---------------- RUN ----------------
DrawApp()
