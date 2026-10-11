import tkinter as tk
from tkinter import filedialog, messagebox

from PIL.ImageTk import PhotoImage
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.backends import default_backend
import os
import time
from PIL import ImageTk, Image
# Global variables to store RSA keys
private_key = None
public_key = None

def browse_file():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        file_name.set(file_path)

def generate_keys():
    global private_key, public_key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

def encrypt_file():
    global private_key, public_key

    # Check if a file is selected
    file_path = file_name.get()
    if not file_path:
        messagebox.showerror("Error", "No file selected.")
        return

    # Read file content
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Generate RSA keys
    generate_keys()

    # Generate a random symmetric key for AES
    aes_key = os.urandom(32)  # 256-bit AES key

    # Encrypt the AES key with the RSA public key
    start_time = time.time()  # Start timing encryption
    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Encrypt the file content with AES
    iv = os.urandom(16)  # Initialization vector for AES
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad the file data to be AES block size compatible
    padder = sym_padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(file_data) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    end_time = time.time()  # End timing encryption

    encryption_time = end_time - start_time  # Calculate time taken for encryption

    # Save encrypted data to a file
    with open("encrypted_file.bin", "wb") as enc_file:
        enc_file.write(encrypted_aes_key + iv + encrypted_data)

    result_text.set(f"File encrypted successfully in {encryption_time:.6f} seconds.\nEncrypted file saved as 'encrypted_file.bin'.")

def decrypt_file():
    global private_key

    # Check if a file is selected
    if not private_key:
        messagebox.showerror("Error", "Private key not generated. Please encrypt a file first.")
        return

    encrypted_file_path = filedialog.askopenfilename(title="Select Encrypted File", filetypes=(("Binary files", "*.bin"), ("All files", "*.*")))
    if not encrypted_file_path:
        messagebox.showerror("Error", "No encrypted file selected.")
        return

    # Read encrypted file content
    with open(encrypted_file_path, "rb") as enc_file:
        file_content = enc_file.read()

    # Extract RSA-encrypted AES key, IV, and encrypted data
    encrypted_aes_key = file_content[:256]  # RSA 2048-bit key = 256 bytes
    iv = file_content[256:272]  # AES block size for IV = 16 bytes
    encrypted_data = file_content[272:]

    # Start timing decryption
    start_time = time.time()

    # Decrypt the AES key with the RSA private key
    aes_key = private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt the file content with AES
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding
    unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    end_time = time.time()  # End timing decryption
    decryption_time = end_time - start_time  # Calculate time taken for decryption

    # Save decrypted data to a file
    with open("decrypted_file.txt", "wb") as dec_file:
        dec_file.write(decrypted_data)

    result_text.set(f"File decrypted successfully in {decryption_time:.6f} seconds.\nDecrypted file saved as 'decrypted_file.txt'.")

# Tkinter GUI
root = tk.Tk()
root.title("RSA Encryption & Decryption")
root.geometry("600x300")
root.configure(bg="#DDEEFF")
file_name = tk.StringVar()
result_text = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.configure(background='#DDEEFF')
frame.pack()

# File selection
browse_button = tk.Button(frame, text="Browse File", command=browse_file)
browse_button.grid(row=0, column=0, padx=5, pady=5)

file_label = tk.Label(frame, textvariable=file_name, wraplength=500, justify="left")
file_label.configure(background='#DDEEFF')
file_label.grid(row=1, column=0, padx=5, pady=5)

# Encrypt and Decrypt buttons
encrypt_button = tk.Button(frame, text="Encrypt File", command=encrypt_file)
encrypt_button.grid(row=3, column=0, padx=5, pady=5)

decrypt_button = tk.Button(frame, text="Decrypt File", command=decrypt_file)
decrypt_button.grid(row=5, column=0, padx=5, pady=5)

# Result display
result_label = tk.Label(frame, textvariable=result_text, wraplength=500, justify="left")
result_label.configure(background='#DDEEFF')
result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
