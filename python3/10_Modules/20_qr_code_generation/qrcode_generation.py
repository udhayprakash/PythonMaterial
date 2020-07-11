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
        Email: uday3prakash@gmail.com
        Phone: +91-9533787794
    '''
    url = pyqrcode.create(message)
    if os.path.exists('QR_CODE.png'):
        os.remove('QR_CODE.png')
    url.png('QR_CODE.png', scale=8)
    # print("Printing QR code")
    # print(url.terminal())


generate_qr()

# future Ref: https://pythonhosted.org/PyQRCode/index.html
