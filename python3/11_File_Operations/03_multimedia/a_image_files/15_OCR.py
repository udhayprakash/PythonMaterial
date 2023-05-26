"""
Purpose: OCR from image

    pip install pytesseract
"""
import pytesseract
from PIL import Image

# print(dir(pytesseract))

# Load the image
image_file = "/workspaces/PythonForDataEngineeringApril2023/11_File_operations/03_multimedia/a_imagefiles/images/pil_text.png"
image = Image.open(image_file)

# Extract text from the image
text = pytesseract.image_to_string(image)
print(text)
