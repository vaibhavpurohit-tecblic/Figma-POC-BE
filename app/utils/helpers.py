import boto3
import os

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('AWS_REGION_NAME')
BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

s3 = boto3.client('s3',
                  aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY,
                  region_name=REGION_NAME)

def upload_directory(directory_name, bucket_name):
    for root, dirs, files in os.walk(directory_name):
        for file in files:
            file_path = os.path.join(root, file)
            # Remove the directory_name prefix and add 'development/' as the prefix
            s3_file_key = f"development/{file_path.replace(directory_name, '', 1).lstrip('/')}"
            try:
                s3.upload_file(file_path, bucket_name, s3_file_key)
                print(f'File "{file_path}" uploaded successfully to bucket "{bucket_name}" as "{s3_file_key}"')
            except Exception as e:
                print(f'Error uploading file "{file_path}": {str(e)}')

if __name__ == '__main__':
    directory_name = 'app/output' 
    upload_directory(directory_name, BUCKET_NAME)
