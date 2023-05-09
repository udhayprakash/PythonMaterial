import boto3

# import os
# session = boto3.Session(
#     aws_access_key_id=os.environ['AWS_SERVER_PUBLIC_KEY'],
#     aws_secret_access_key=os.environ['AWS_SERVER_SECRET_KEY'],
# )

# pip install awscli
# aws configure

# ref: https://blog.gitguardian.com/how-to-handle-aws-secrets/

session = boto3.Session()

print(
    f"""
    {session                            =}
    {session.profile_name               =}
    {session.available_profiles         =}
    {session.region_name                =}
    {session.get_available_partitions() =}
    {session.get_available_resources()  =}
    {session.get_available_services()   =}
"""
)

creds = session.get_credentials()
print(
    f"""
    {creds.access_key =}
"""
)  # {creds.secret_key =}

# Its recommended to create own session
import boto3.session

# Create your own session
my_session = boto3.session.Session()
print(session, my_session)
