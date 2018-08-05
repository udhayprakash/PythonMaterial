from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image

# -size 320x100 xc:lightblue
with Image(width=320, height=100, background=Color('lightblue')) as image:
    with Drawing() as draw:
        # -font Candice
        draw.font = 'Candice'
        # -pointsize 72
        draw.font_size = 72.0
        draw.push()
        # -fill black
        draw.fill_color = Color('black')
        # -draw "text 28,68 'Udhay'"
        draw.text(28, 68, 'Udhay')
        draw.pop()
        draw.push()
        # -fill white
        draw.fill_color = Color('white')
        # -draw "text 25,65 'Udhay'"
        draw.text(25, 65, 'Udhay')
        draw.pop()
        draw(image)
    # font_shadow.jpg
    image.save(filename='font_shadow.jpg')