import io

from reportlab.pdfgen import canvas


def lambda_handler(event, context):
    # Create the PDF file in memory
    pdf_bytes = io.BytesIO()
    pdf_canvas = canvas.Canvas(pdf_bytes)
    pdf_canvas.drawString(100, 750, "Hello, World!")
    pdf_canvas.save()

    # Get the bytes of the PDF file and return it as the response
    pdf_data = pdf_bytes.getvalue()

    return {
        "statusCode": 200,
        "body": pdf_data,
        "headers": {
            "Content-Type": "application/pdf",
            "Content-Disposition": 'attachment; filename="hello.pdf"',
        },
    }
