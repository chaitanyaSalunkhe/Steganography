### encrypt.py
import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

def encrypt_message(image_path, message, password, output_path):
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Invalid image file!")
        return
    
    full_message = password + "||" + message  # Combine password and message
    binary_message = ''.join(format(ord(c), '08b') for c in full_message) + '1111111111111110'  # End delimiter
    data_index = 0
    
    for row in img:
        for pixel in row:
            for channel in range(3):  # RGB Channels
                if data_index < len(binary_message):
                    new_value = (int(pixel[channel]) & ~1) | int(binary_message[data_index])
                    pixel[channel] = np.uint8(max(0, min(255, new_value)))  # Ensure valid uint8 range
                    data_index += 1
                else:
                    break
    
    cv2.imwrite(output_path, img)
    messagebox.showinfo("Success", "Message encrypted successfully!")

def encrypt_gui():
    root = tk.Tk()
    root.title("Encrypt Message")
    
    tk.Label(root, text="Select Image:").pack()
    img_path = tk.Entry(root, width=50)
    img_path.pack()
    tk.Button(root, text="Browse", command=lambda: img_path.insert(0, filedialog.askopenfilename())).pack()
    
    tk.Label(root, text="Enter Message:").pack()
    msg_entry = tk.Entry(root, width=50)
    msg_entry.pack()
    
    tk.Label(root, text="Enter Password:").pack()
    pass_entry = tk.Entry(root, width=50, show="*")
    pass_entry.pack()
    
    tk.Button(root, text="Encrypt", command=lambda: encrypt_message(img_path.get(), msg_entry.get(), pass_entry.get(), "encryptedImage.png")).pack()
    
    root.mainloop()

if __name__ == "__main__":
    encrypt_gui()