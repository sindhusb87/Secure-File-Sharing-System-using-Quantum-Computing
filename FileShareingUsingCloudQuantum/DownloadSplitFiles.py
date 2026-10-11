import os
from dotenv import load_dotenv
load_dotenv()
import boto3


def download_from_s3(bucket_name, file_name, download_path, aws_access_key, aws_secret_key):
    """
    Download a file from S3.

    :param bucket_name: Name of the S3 bucket
    :param file_name: The name of the file in the bucket
    :param download_path: The local path where the file will be saved
    :param aws_access_key: Your AWS access key
    :param aws_secret_key: Your AWS secret key
    """
    # Initialize S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )

    # Download the file
    s3.download_file(bucket_name, file_name, download_path)
    print(f"File {file_name} downloaded to {download_path}")


# Example usage

file_name = "extramyfile.txt"  # Replace with the name of the file you want to download
download_path = "downloadedfiles/"  # Local path to save the downloaded file
bucket_name = "ccquantumbucket"
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

# Download the file
for i in range(1, 6):
    newfile = f"{file_name}_part_{i}.txt"
    print(newfile)
    download_path = "downloadedfiles/"+newfile

    download_from_s3(bucket_name, newfile, download_path, aws_access_key, aws_secret_key)
