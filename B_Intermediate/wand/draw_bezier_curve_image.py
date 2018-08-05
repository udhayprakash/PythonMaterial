from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
    draw.stroke_color = Color('black')
    draw.stroke_width = 2
    draw.fill_color = Color('white')
    points = [(10,50),  # Start point
              (50,10),  # First control
              (50,90),  # Second control
              (90,50)]  # End point
    draw.bezier(points)
    with Image(width=100,
               height=100,
               background=Color('lightblue')) as image:
        draw(image)