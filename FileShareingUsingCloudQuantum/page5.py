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
class Page5(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.background_image = tk.PhotoImage(file="bg.png")  # Replace with your image path
        # Create a label to display the background image
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)




        # Title label
        tk.Label(self, text="S3 Bucket Name:").pack(pady=5)
        self.bucket_name_entry = tk.Entry(self, width=30, text="ccquantumbucket")
        self.bucket_name_entry.pack(pady=5)

        # Button to browse and select file for upload
        self.file_path = None
        self.select_file_btn = tk.Button(self, text="Browse File", command=self.browse_file)
        self.select_file_btn.pack(pady=10)

        # Upload button
        upload_btn = tk.Button(self, text="Upload to S3", command=self.upload_file)
        upload_btn.pack(pady=10)

        #Split_upload_btn = tk.Button(self, text="Upload to S3 by splitting file", command=self.split_upload_file)
        #Split_upload_btn.pack(pady=10)

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(title="Select file to upload")
        if self.file_path:
            messagebox.showinfo("File Selected", f"File selected: {self.file_path}")

    def upload_to_s3(file_paths, bucket_name, aws_access_key, aws_secret_key):
        # Initialize S3 client
        s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

        for file_path in file_paths:
            # Extract the filename
            file_name = file_path.split('/')[-1]

            # Upload file to S3
            s3.upload_file(file_path, bucket_name, file_name)
            print(f"Uploaded {file_name} to bucket {bucket_name}")






    def upload_file(self):
        # -----------------------------------------

        bucket_name = self.bucket_name_entry.get()

        if not bucket_name or not self.file_path:
            messagebox.showwarning("Input Error", "Please enter bucket name and select a file.")
            return

        try:
            file_name = os.path.basename(self.file_path)
            s3_client.upload_file(self.file_path, bucket_name, file_name)
            messagebox.showinfo("Success", f"'{file_name}' uploaded to bucket '{bucket_name}' successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to upload file: {e}")



