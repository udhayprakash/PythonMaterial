"""
fonts can be downloaded from https://www.wfonts.com/font/arial
"""

from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGB", (100, 30), color=(73, 109, 137))

fnt = ImageFont.truetype("/ariali.ttf", 15)

d = ImageDraw.Draw(img)
d.text((10, 10), "Hello world", font=fnt, fill=(255, 255, 0))

img.save("images/pil_text_font.png")


# Example 2
window_height, window_width = 10, 10

img2 = Image.new("L", (window_height, window_width), color="white")

draw = ImageDraw.Draw(img2)

font = ImageFont.truetype("arial", 24)
draw.text((0, 0), "Hello world", font=font)

img2.save("images/ pil_text_font2.jpg")
