from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
    draw.stroke_color = Color('black')
    draw.stroke_width = 2
    draw.fill_color = Color('white')
    draw.circle((50, 50), # Center point
                (25, 25)) # Perimeter point
    with Image(width=100, height=100, background=Color('lightblue')) as image:
        draw(image)