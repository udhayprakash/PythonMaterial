from PIL import Image


def resize_image(input_image_path, output_image_path, new_size):
    original_image = Image.open(input_image_path)

    width, height = original_image.size
    print(f"The original image size is {width} wide x {height} high")

    resized_image = original_image.resize(new_size)

    width, height = resized_image.size
    print(f"The resized image size is {width} wide x {height} high")

    resized_image.show()
    resized_image.save(output_image_path)


if __name__ == "__main__":
    resize_image(
        input_image_path="images/cameraman.jpg",
        output_image_path="images/cameraman_small.jpg",
        new_size=(800, 400),
    )
