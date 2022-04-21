import boto3
from botocore import UNSIGNED
from botocore.client import Config

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
# Use the client


# ref - https://stackoverflow.com/questions/34865927/can-i-use-boto3-anonymously
