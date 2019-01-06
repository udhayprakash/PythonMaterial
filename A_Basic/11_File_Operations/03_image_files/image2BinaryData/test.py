from PIL import Image, ImageFilter
from numpy import array
import numpy as np
image = Image.open("A.png")
# arr = array(image)
# a = np.array(arr)
# # mask = np.all(a==[255,255,255,255])
# # a[mask] = 0
# a[a==[255,255,255,255]] = 0
# print a[0]
width, height = image.size
# print width, height
rgb_im = image.convert('RGB')
image_array =[]
for i in range(0,height):
	x_array = []
	for j in range(0,width):
		if rgb_im.getpixel((i, j)) == (0,0,0):
			x_array.append(1)
		else: 
			x_array.append(0)
	image_array.append(x_array)
# print image_array
a = np.array(image_array)
print a
