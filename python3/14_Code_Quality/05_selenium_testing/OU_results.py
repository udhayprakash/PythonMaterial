#!/usr/bin/python
"""
Purpose: TO get the  OU examination results

http://www.osmania.ac.in/res07/20180472.jsp

Hall ticket numbers
	160314732001, 160314732005
"""

import requests
from pprint import pprint

response = requests.post("http://www.osmania.ac.in/res07/20180472.jsp")

print(response.text)
