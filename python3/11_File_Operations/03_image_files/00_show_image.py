#!/usr/bin/python
"""

pip install -U pillow --user
"""
from PIL import Image

my_image = Image.open('images/cameraman.jpg')
my_image.show()

# Get Image information
def get_image_info(path):
    image = Image.open(path)
    print(f'This image is {image.width} x {image.height}')
    exif = image._getexif()
    print(f'exif of {path} is {exif}')

get_image_info('images/cameraman.jpg')
get_image_info('images/python.jpg')

import matplotlib.pyplot as plt

def get_image_histrogram(path):
    image = Image.open(path)
    histogram = image.histogram()
    plt.hist(histogram, bins=len(histogram))
    plt.xlabel('Histogram')
    plt.show()

get_image_histrogram('images/cameraman.jpg')
get_image_histrogram('images/python.jpg')
