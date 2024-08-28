import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

def swap_pixels(image_array):
    return np.flipud(np.fliplr(image_array))

def process_image(action):
    global img
    if img is None:
        messagebox.showerror("Error", "No image loaded.")
        return
    
    image_array = np.array(img)
    processed_array = swap_pixels(image_array)
    processed_img = Image.fromarray(processed_array)
    processed_img.save(f"{action}_image.png")
    processed_img.show()

def load_image():
    global img
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk


root = tk.Tk()
root.title("Image Encryption Tool")

img = None

tk.Button(root, text="Load Image", command=load_image).pack(padx=10, pady=5)
tk.Button(root, text="Encrypt", command=lambda: process_image('encrypt')).pack(padx=10, pady=5)
tk.Button(root, text="Decrypt", command=lambda: process_image('decrypt')).pack(padx=10, pady=5)

image_label = tk.Label(root)
image_label.pack(padx=10, pady=5)

root.mainloop()
