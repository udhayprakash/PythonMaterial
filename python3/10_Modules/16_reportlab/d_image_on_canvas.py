#!/usr/bin/python3

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def add_image(image_path):
    my_canvas = canvas.Canvas("d_image_on_canvas.pdf", pagesize=letter)
    my_canvas.drawImage(image_path, 30, 600, width=100, height=100)
    my_canvas.save()


if __name__ == "__main__":
    image_path = "python_logo.png"
    add_image(image_path)
