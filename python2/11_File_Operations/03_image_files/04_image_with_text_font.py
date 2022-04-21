from PIL import Image, ImageDraw, ImageFont

"""
fonts can be downloaded from https://www.wfonts.com/font/arial
"""

img = Image.new('RGB', (100, 30),
                color = (73, 109, 137))

fnt = ImageFont.truetype('/ariali.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10,10), 'Hello world', font=fnt, fill=(255, 255, 0))

img.save('pil_text_font.png')
