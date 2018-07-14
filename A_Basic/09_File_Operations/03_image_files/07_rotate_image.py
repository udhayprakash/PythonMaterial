from PIL import Image

original_image = Image.open("strawberries.png")
original_image.show()

rotated_image = original_image.rotate(45)
rotated_image.show()
