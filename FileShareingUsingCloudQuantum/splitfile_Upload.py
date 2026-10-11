import os
from dotenv import load_dotenv
load_dotenv()
import boto3


def split_file(file_path, parts=5):
    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Calculate number of lines per part
    total_lines = len(lines)
    lines_per_part = total_lines // parts
    extra_lines = total_lines % parts  # Handle remainder

    file_parts = []
    start = 0
    for i in range(parts):
        # Determine end line index for the part
        end = start + lines_per_part + (1 if i < extra_lines else 0)
        part_filename = f"{file_path}_part_{i + 1}.txt"

        # Write the split part to a new file
        with open(part_filename, 'w') as part_file:
            part_file.writelines(lines[start:end])

        file_parts.append(part_filename)
        start = end

    return file_parts


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


# Example usage
file_path = "extramyfile.txt"
bucket_name = "ccquantumbucket"
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

# Step 1: Split the file into parts
file_parts = split_file(file_path)

# Step 2: Upload each part to S3
upload_to_s3(file_parts, bucket_name, aws_access_key, aws_secret_key)
