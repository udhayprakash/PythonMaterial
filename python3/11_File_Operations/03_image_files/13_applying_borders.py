#!/usr/bin/python3


from PIL import Image, ImageOps


def add_border(input_image, output_image, border):
    img = Image.open(input_image)
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border)
    else:
        raise RuntimeError("Border is not an integer or tuple!")
    bimg.save(output_image)


def add_color_border(input_image, output_image, border, color=0):
    img = Image.open(input_image)
    if isinstance(border, int) or isinstance(
        border, tuple):
        bimg = ImageOps.expand(img,
                               border=border, 
                               fill=color)
    else:
        msg = 'Border is not an integer or tuple!'
        raise RuntimeError(msg)
    bimg.save(output_image)

if __name__ == "__main__":
    add_border('images/butterfly.png', 
            output_image='images/butterfly_border.png', border=100)
    add_color_border('images/butterfly.png', 
            output_image='images/butterfly_color_border.png', border=100,
               color='indianred')
