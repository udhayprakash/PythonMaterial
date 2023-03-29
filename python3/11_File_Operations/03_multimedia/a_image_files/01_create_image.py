#!/usr/bin/python
"""

pip install pillow
"""

from PIL import Image, ImageDraw

img = Image.new("RGB", (600, 30), color="red")
#                mode,  size,    color

img.save("images/pil_red.png")
