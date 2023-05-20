import boto3


def fetch_secret_from_aws(secret_name):
    try:
        session = boto3.session.Session()
        client = session.client(service_name="secretsmanager", region_name="us-east-1")
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        return get_secret_value_response["SecretString"]
    except Exception as e:
        print(e)
        return None


def create_secret_in_aws(secret_name, secret_value):
    try:
        session = boto3.session.Session()
        client = session.client(service_name="secretsmanager", region_name="us-east-1")
        client.create_secret(Name=secret_name, SecretString=secret_value)
        return True
    except Exception as e:
        print(e)
        return False
