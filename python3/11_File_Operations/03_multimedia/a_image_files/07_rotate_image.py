from PIL import Image

original_image = Image.open("images/strawberries.png")
original_image.show()

rotated_image = original_image.rotate(45)
rotated_image.show()

rotated_image = original_image.rotate(90)
rotated_image.show()

rotated_image = original_image.rotate(180)
rotated_image.show()
