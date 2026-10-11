import os
from dotenv import load_dotenv
load_dotenv()
import os
import tkinter as tk
from tkinter import messagebox, filedialog

import boto3
s3_client = boto3.client(
            's3',
            region_name='ap-south-1',
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
        )
class Page6(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.background_image = tk.PhotoImage(file="bg.png")  # Replace with your image path
        # Create a label to display the background image
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)



        tk.Label(self, text="S3 Bucket Name:").pack(pady=5)
        self.bucket_name_entry = tk.Entry(self, width=30)
        self.bucket_name_entry.pack(pady=5)

        # File name input
        tk.Label(self, text="File Name on S3:").pack(pady=5)
        self.file_key_entry = tk.Entry(self, width=30)
        self.file_key_entry.pack(pady=5)

        # Download button
        download_btn = tk.Button(self, text="Download from S3", command=self.download_file)
        download_btn.pack(pady=10)

    def download_file(self):

        bucket_name = self.bucket_name_entry.get()

        bucket_name = self.bucket_name_entry.get()
        file_key = self.file_key_entry.get()

        if not bucket_name or not file_key:
            messagebox.showwarning("Input Error", "Please provide both bucket name and file name.")
            return

        save_path = filedialog.askdirectory(title="Select folder to save the downloaded file")
        if not save_path:
            return

        try:
            download_path = os.path.join(save_path, file_key)
            s3_client.download_file(bucket_name, file_key, download_path)
            messagebox.showinfo("Success", f"'{file_key}' downloaded to '{download_path}' successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download file: {e}")
    pass



