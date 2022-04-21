#!/usr/bin/python
"""
Purpose: To remove exif data from image
"""

from PIL import Image

SOURCE_IMAGE = "images/cameraman.jpg"
TARGET_IMAGE = "images/cameraman_file_without_exif.jpeg"


image = Image.open(SOURCE_IMAGE)

# next 3 lines strip exif
data = list(image.getdata())
image_without_exif = Image.new(image.mode, image.size)
image_without_exif.putdata(data)

image_without_exif.save(TARGET_IMAGE)
