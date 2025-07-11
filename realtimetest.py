import tkinter as tk
from PIL import ImageGrab, ImageOps
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("D:\coding\digit-recognition\mnist_cnn_model.h5")

# Setup canvas
canvas_width = 200
canvas_height = 200

root = tk.Tk()
root.title("Draw a Digit")

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Draw with mouse
def draw(event):
    x, y = event.x, event.y
    r = 8
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")

canvas.bind("<B1-Motion>", draw)

# Predict
def predict_digit():
    # Grab canvas content
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas_width
    y1 = y + canvas_height
    img = ImageGrab.grab().crop((x, y, x1, y1)).convert('L')  # grayscale

    # Invert image: MNIST is white background, black digit
    img = ImageOps.invert(img)

    # Resize to 28x28
    img = img.resize((28, 28))

    # Apply binary threshold (improve contrast)
    img = img.point(lambda x: 0 if x < 128 else 255, '1')
    img = img.convert('L')

    # Normalize and reshape
    img = np.array(img).astype('float32') / 255.0
    img = img.reshape(1, 28, 28, 1)

    # Predict
    pred = model.predict(img)
    digit = np.argmax(pred)

    result_label.config(text=f"Prediction: {digit}")


# Buttons
btn_predict = tk.Button(root, text="Predict", command=predict_digit)
btn_predict.pack()

btn_clear = tk.Button(root, text="Clear", command=lambda: canvas.delete("all"))
btn_clear.pack()

result_label = tk.Label(root, text="Draw a digit and click Predict", font=("Helvetica", 14))
result_label.pack()

root.mainloop()
