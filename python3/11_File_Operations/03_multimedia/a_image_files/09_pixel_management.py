from PIL import Image

original_image = Image.open("images/strawberries.png")

width, height = original_image.size

for x in range(width):
    for y in range(height):
        pixel_coordinate = (x, y)
        r, g, b, alpha = original_image.getpixel(pixel_coordinate)

        negative_color = (255 - r, 255 - g, 255 - b)
        original_image.putpixel(pixel_coordinate, negative_color)

original_image.show()
original_image.save("images/result.png")
