#!/usr/bin/python3

from reportlab.pdfgen import canvas

c = canvas.Canvas("a_create_pdf.pdf")
c.drawString(100, 750, "Welcome to Reportlab!")
c.save()
