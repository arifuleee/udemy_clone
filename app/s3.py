import boto3
from botocore.exceptions import NoCredentialsError

def upload_video_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name or file_name)
    except FileNotFoundError:
        return "The file was not found"
    except NoCredentialsError:
        return "Credentials not available"
    return f"https://{bucket}.s3.amazonaws.com/{object_name or file_name}"
