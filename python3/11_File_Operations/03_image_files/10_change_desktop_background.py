#!/usr/bin/python
"""
Purpose: TO change the desktop background
"""
import ctypes
import os

drive = './'
folder = ''
image = 'images/cameraman.jpg'
image_path = os.path.join(drive, folder, image)
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
