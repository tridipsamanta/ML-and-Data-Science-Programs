import tensorflow as tf
import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw
import os

# -------- LOAD MNIST --------
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

# -------- BUILD CNN --------
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

# -------- TRAIN --------
model.fit(x_train, y_train, epochs=3, validation_data=(x_test, y_test))

# -------- GUI --------
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
        r = 8
        x, y = event.x, event.y
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="white", outline="white")
        self.draw.ellipse((x-r, y-r, x+r, y+r), fill="white")

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle((0, 0, 280, 280), fill="black")

    def predict(self):
        img = self.image.resize((28, 28))
        img = np.array(img) / 255.0
        img = img.reshape(1, 28, 28)

        pred = np.argmax(model.predict(img), axis=1)[0]

        tk.messagebox.showinfo("Prediction", f"Predicted Digit: {pred}")

# -------- RUN --------
DrawApp()
