#!/usr/bin/python
"""

pip install -U pillow --user
"""
from PIL import Image

my_image = Image.open('images/cameraman.jpg')
my_image.show()
