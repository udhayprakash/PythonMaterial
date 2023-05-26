from PIL import Image


def crop_image(path, cropped_path):
    image = Image.open(path)
    image.show()
    cropped = image.crop((40, 590, 979, 1500))

    # x and y coordinates relative to top left corner
    cropped.save(cropped_path)
    cropped.show()


if __name__ == "__main__":
    crop_image("images/strawberries.png", "images/strawberries_cropped.png")
