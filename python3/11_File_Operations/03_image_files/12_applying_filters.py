#!/usr/bin/python3
"""
Purpose: Applying filters on Images
    BLUR
    CONTOUR
    DETAIL
    EDGE_ENHANCE
    EDGE_ENHANCE_MORE
    EMBOSS
    FIND_EDGES
    SHARPEN
    SMOOTH
    SMOOTH_MORE`
"""

from PIL import Image, ImageFilter


def blur(path, modified_photo):
    image = Image.open(path)
    blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.save(modified_photo)


def sharpen(path, modified_photo):
    image = Image.open(path)
    sharpened_image = image.filter(ImageFilter.SHARPEN)
    sharpened_image.save(modified_photo)


if __name__ == "__main__":
    blur("images/butterfly.png", "images/butterfly_blurred.png")
    blur("images/butterfly.png", "images/butterfly_sharper.png")
