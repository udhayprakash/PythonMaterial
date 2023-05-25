"""
Purpose: OCR from image

    pip install pytesseract
"""
import pytesseract

# Import the necessary libraries
from PIL import Image

# Load the image
image_file = r"C:\Users\Amma\Downloads\prob1b.jpg"
image = Image.open(image_file)

# Extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
