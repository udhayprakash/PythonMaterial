#!/usr/bin/python
"""

pip install pillow
"""
from PIL import Image

my_image = Image.open('cameraman.jpg')
my_image.show()
