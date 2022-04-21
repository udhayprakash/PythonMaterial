#!/usr/bin/python

from PIL import Image

size = width, height = 320, 240
#image = Image.new("RGB", size)   # by default, it is black color
#image = Image.new("RGB", size, "white")
#image = Image.new("RGB", size, "red")
image = Image.new('RGB', size, 'salmon')
#image = Image.new("L", size, "hsl(0,100%, 50%)")
image.show()

del image
