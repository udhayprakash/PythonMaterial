#!/usr/bin/python
"""
Purpose: dotenv module

    pip install -U python-dotenv --user

"""
import os
from pathlib import Path  # Python 3.6+ only

import dotenv

print(f"{dotenv.find_dotenv() =}")
# recognizes .env in current directory, if not specified

# To load the .env file
# dotenv.load_dotenv()
# dotenv.load_dotenv(verbose=True)
# dotenv.load_dotenv(dotenv.find_dotenv())

# # OR, explicitly providing path to '.env'
env_path = Path(".") / ".env"
dotenv.load_dotenv(dotenv_path=env_path)

# Accessing the .env file keys
print(
    f"""
    {os.getenv('REDIS_ADDRESS')   =}
    {os.getenv('MEANING_OF_LIFE') =}
    {os.getenv('MULTILINE_VAR')   =}

    {os.getenv('S3_BUCKET')       =}
    {os.getenv('SECRET_KEY')      =}

    {os.getenv('server')          =}
    {os.getenv('port')            =}
    {os.getenv('url_format')      =}
    {os.getenv('url')             =}
"""
)
# NOTE:
# 1. load_dotenv does not override existing System environment variables.
# 2. To override, pass override=True to load_dotenv()


# To set a environment variable in .env file
# dotenv.set_key('.', 'name', 'Udhay')
