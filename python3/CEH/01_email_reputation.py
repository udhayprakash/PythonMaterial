#!/usr/bin/python
"""
Purpose: API to get the reputation of an Email
"""
import requests
from pprint import pprint


def get_report_on_email(_email):
    response = requests.get(f'http://emailrep.io/{_email}')
    pprint(response.json())
    return response.json()


if __name__ == '__main__':
    get_report_on_email('uday3prakash@gmail.com')
    get_report_on_email('udhay@mailinator.com')
    # get_report_on_email('bsheffield432@gmail.com')
