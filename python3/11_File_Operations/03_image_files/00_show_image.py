#!/usr/bin/python
"""

pip install -U pillow --user
"""
import matplotlib.pyplot as plt
from PIL import Image

my_image = Image.open("images/cameraman.jpg")
my_image.show()


def get_image_info(path):
    """To Get Image information"""
    image = Image.open(path)
    print(f"This image is {image.width} x {image.height}")
    exif = image._getexif()
    print(f"exif of {path} is {exif}")


get_image_info("images/cameraman.jpg")
get_image_info("images/python.jpg")


def get_image_histrogram(path):
    image = Image.open(path)
    histogram = image.histogram()
    plt.hist(histogram, bins=len(histogram))
    plt.xlabel("Histogram")
    plt.show()


get_image_histrogram("images/cameraman.jpg")
get_image_histrogram("images/python.jpg")
