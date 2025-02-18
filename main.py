### main.py
import tkinter as tk
import os

def open_encrypt():
    os.system("python encrypt.py")

def open_decrypt():
    os.system("python decrypt.py")

def main_gui():
    root = tk.Tk()
    root.title("Image Encryption & Decryption")
    
    tk.Label(root, text="Select an option:").pack(pady=10)
    btn_encrypt = tk.Button(root, text="Encrypt a Message", command=open_encrypt)
    btn_encrypt.pack(pady=10)
    
    btn_decrypt = tk.Button(root, text="Decrypt a Message", command=open_decrypt)
    btn_decrypt.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()
