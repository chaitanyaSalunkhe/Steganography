### decrypt.py
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

def decrypt_message(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Invalid image file!")
        return
    
    binary_message = ""
    for row in img:
        for pixel in row:
            for channel in range(3):  # RGB Channels
                binary_message += str(int(pixel[channel]) & 1)
    
    binary_chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ""
    for char in binary_chars:
        if char == '11111110':  # End delimiter detected
            break
        message += chr(int(char, 2))
    
    if "||" in message:
        stored_password, stored_message = message.split("||", 1)
        if password == stored_password:
            messagebox.showinfo("Decrypted Message", stored_message)
        else:
            messagebox.showerror("Error", "Incorrect password!")
    else:
        messagebox.showerror("Error", "Invalid data format!")

def decrypt_gui():
    root = tk.Tk()
    root.title("Decrypt Message")
    
    tk.Label(root, text="Select Encrypted Image:").pack()
    img_path = tk.Entry(root, width=50)
    img_path.pack()
    tk.Button(root, text="Browse", command=lambda: img_path.insert(0, filedialog.askopenfilename())).pack()
    
    tk.Label(root, text="Enter Password:").pack()
    pass_entry = tk.Entry(root, width=50, show="*")
    pass_entry.pack()
    
    tk.Button(root, text="Decrypt", command=lambda: decrypt_message(img_path.get(), pass_entry.get())).pack()
    
    root.mainloop()

if __name__ == "__main__":
    decrypt_gui()