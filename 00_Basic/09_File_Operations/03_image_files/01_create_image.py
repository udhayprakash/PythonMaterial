from PIL import Image, ImageDraw

img = Image.new('RGB', (60, 30), color = 'red')
#                mode,  size,    color

img.save('pil_red.png')
