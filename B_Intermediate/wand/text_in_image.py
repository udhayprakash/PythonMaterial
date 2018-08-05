from wand.color import Color
from wand.compat import nested
from wand.drawing import Drawing
from wand.image import Image

dimensions = {'width': 450,
              'height': 100}

with nested(Image(background=Color('skyblue'), **dimensions),
            Image(background=Color('transparent'), **dimensions)) as (bg, shadow):
    # Draw the drop shadow
    with Drawing() as ctx:
        ctx.fill_color = Color('rgba(3, 3, 3, 0.6)')
        ctx.font_size = 64
        ctx.text(50, 75, 'Hello Wand!')
        ctx(shadow)
    # Apply filter
    shadow.gaussian_blur(4, 2)
    # Draw text
    with Drawing() as ctx:
        ctx.fill_color = Color('firebrick')
        ctx.font_size = 64
        ctx.text(48, 73, 'Hello Wand!')
        ctx(shadow)
    bg.composite(shadow, 0, 0)
    bg.save(filename='out.png')