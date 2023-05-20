"""
Purpose:
    hvac (Python client for Vault) installed and have a Hashicorp Vault setup.

    https://pypi.org/project/hvac/

"""
import hvac


def read_secret_from_vault(secret_path, token, secret_name):
    try:
        client = hvac.Client(
            url="http://localhost:8200",
            token=token,
        )
        read_response = client.secrets.kv.read_secret_version(path=secret_path)
        return read_response["data"]["data"][secret_name]
    except Exception as e:
        print(e)
        return None


def write_secret_to_vault(secret_path, token, secret_name, secret_value):
    try:
        client = hvac.Client(
            url="http://localhost:8200",
            token=token,
        )
        create_response = client.secrets.kv.v2.create_or_update_secret(
            path=secret_path,
            secret={secret_name: secret_value},
        )
        return create_response
    except Exception as e:
        print(e)
        return None
