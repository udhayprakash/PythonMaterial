from PIL import Image

original_image = Image.open("images/strawberries.png")

rotated_image = original_image.rotate(45)
rotated_image.save("images/strawberries_45.png")

rotated_image = original_image.rotate(90)
rotated_image.save("images/strawberries_90.png")

rotated_image = original_image.rotate(180)
rotated_image.save("images/strawberries_180.png")
