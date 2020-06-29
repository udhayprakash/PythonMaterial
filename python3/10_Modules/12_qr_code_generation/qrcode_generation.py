#!/usr/bin/python
"""
Purpose: To generate QR Code 

pip install pyqrcode pypng --user
"""
import os
import pyqrcode


def generate_qr():
    message = ''' 
        Name: Udhay Prakash
        Blog: https://udhayprakash.blogspot.com/
    '''
    url = pyqrcode.create(message)
    if os.path.exists('url.png'):
        os.remove('url.png')
    url.png('url.png', scale=8)
    # print("Printing QR code")
    # print(url.terminal())


generate_qr()

# future Ref: https://pythonhosted.org/PyQRCode/index.html
