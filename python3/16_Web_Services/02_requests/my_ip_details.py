#!/usr/bin/python
"""
Purpose:
    https://ipapi.co/
"""

import requests


# response = requests.get('https://ipapi.co/')
# with open('ipapi.html', 'w') as f:
#     f.write(response.text)
#     f.close()
#
# response = requests.get('https://ipapi.co/json')
# with open('ipapi.json', 'w') as f:
#     f.write(response.text)
#     f.close()
#
# response = requests.get('https://ipapi.co/xml')
# with open('ipapi.xml', 'w') as f:
#     f.write(response.text)
#     f.close()
#
# response = requests.get('https://ipapi.co/yaml')
# with open('ipapi.yaml', 'w') as f:
#     f.write(response.text)
#     f.close()

def get_my_ip_details():
    for ech_extn in ('html', 'json', 'yaml', 'csv'):
        file_name = 'ipapi.' + ech_extn
        if ech_extn == 'html':
            ech_extn = ''
        URL = 'https://ipapi.co/' + ech_extn

        response = requests.get(URL)
        with open(file_name, 'w') as f:
            f.write(response.text)
            f.close()


if __name__ == '__main__':
    get_my_ip_details()
