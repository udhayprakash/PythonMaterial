from PIL import Image

original_image = Image.open('strawberries.png')
# original_image = Image.open("cameraman.jpg")

width, height = original_image.size

for x in range(width):
    for y in range(height):
        pixel_coordinate = (x,y)
        r,g,b, alpha = original_image.getpixel(pixel_coordinate)

        negative_color = (255-r, 255-g, 255-b)
        original_image.putpixel(pixel_coordinate, negative_color)


original_image.show()
