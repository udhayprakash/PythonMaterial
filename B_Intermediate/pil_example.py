#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont

# Text positioning
text_y = 100
text_pad = 45

# Define fonts for regular text and heading
# data_font = ImageFont.truetype("Roboto-Regular.ttf", 32)
# header_font = ImageFont.truetype("Roboto-Bold.ttf", 50)

# Load background image
bg_img = Image.open("bg_img.png")
surface = ImageDraw.Draw(bg_img)

# Write heading
# surface.text((20, 8), "Temperature Log", font=header_font)

# Write temperatures
for x in range(len(temps)):
    surface.text((20, (text_y + (text_pad * x))), temps[x], font=data_font)

# Save file
bg_img.save(open("temp_log.png", "wb"), "PNG")