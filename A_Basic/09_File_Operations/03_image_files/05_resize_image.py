from PIL import Image


def resize_images(image_names, new_size=(200, 200)):
    for image_name in image_names:
        img = Image.open(image_name)
        img = img.resize(new_size)
        img.save("resized_" + image_name)


images = ["cameraman.jpg", "strawberries.png", "python.jpg"]

resize_images(images)
