import os

import boto3
import dotenv

dotenv.load_dotenv(".env")

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('AWS_REGION_NAME')
BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

s3 = boto3.client('s3',
                  aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY,
                  region_name=REGION_NAME)


def get_content_type(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.svg':
        return 'image/svg+xml'
    elif file_extension == '.png':
        return 'image/png'
    elif file_extension == '.jpg' or file_extension == '.jpeg':
        return 'image/jpeg'
    elif file_extension == '.html':
        return 'text/html'
    else:
        return 'application/octet-stream'


def upload_directory(local_directory, bucket_name, s3_prefix=''):
    for root, dirs, files in os.walk(local_directory):
        for file in files:
            file_path = os.path.join(root, file)
            s3_file_key = f"{s3_prefix}{file_path.replace(local_directory, '', 1).lstrip('/')}"
            content_type = get_content_type(file_path)
            try:
                s3.upload_file(file_path, bucket_name, s3_file_key, ExtraArgs={'ContentType': content_type})
                print(
                    f'File "{file_path}" uploaded successfully to bucket "{bucket_name}" as "{s3_file_key}" with content type "{content_type}"')
            except Exception as e:
                print(f'Error uploading file "{file_path}": {str(e)}')


if __name__ == '__main__':
    local_path = 'app/output'
    s3_path = 'development/'
    upload_directory(local_path, BUCKET_NAME, s3_prefix=s3_path)
