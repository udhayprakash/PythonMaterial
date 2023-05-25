from PIL import Image
from PIL.ExifTags import TAGS


def get_exif_data(image_path):
    """
    Extracts Exif data from an image.

    Args:
    - image_path: A string representing the path to the image file.

    Returns:
    - A dictionary containing the Exif data.
    """
    with Image.open(image_path) as image:
        exifdata = image.getexif()
        exif = {}
        for tag_id in exifdata:
            print(tag_id)
            tag = TAGS.get(tag_id, tag_id)
            value = exifdata.get(tag_id)
            if isinstance(value, bytes):
                value = value.decode()
            exif[tag] = value
    return exif


# Example usage
get_exif_data(r"C:\users\amma\Downloads\naniannayya.jpg")
