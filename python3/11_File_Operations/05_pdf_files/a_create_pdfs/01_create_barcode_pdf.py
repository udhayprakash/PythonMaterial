from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


# ----------------------------------------------------------------------
def createBarcode(path):
    """
    Demo to show how to embed a barcode font
    """
    style = getSampleStyleSheet()
    width, height = letter
    c = canvas.Canvas(path, pagesize=letter)
    barcode_font = r"/free3of9.ttf"
    pdfmetrics.registerFont(TTFont("Free 3 of 9 Regular", barcode_font))

    barcode_string = '<font name="Free 3 of 9 Regular" size="16">%s</font>'
    barcode_string = barcode_string % "1234567890"

    p = Paragraph(barcode_string, style=style["Normal"])
    p.wrapOn(c, width, height)
    p.drawOn(c, 20, 750, mm)

    c.save()


if __name__ == "__main__":
    createBarcode(r"/barcode.pdf")
