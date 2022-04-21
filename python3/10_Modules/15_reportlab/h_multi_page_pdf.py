from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def create_document():
    doc = SimpleDocTemplate('h_multi_page_pdf.pdf',
                            pagesize=letter)
    styles = getSampleStyleSheet()
    flowables = []
    spacer = Spacer(1, 0.25*inch)

    # Create a lot of content to make a multipage PDF
    for i in range(50):
        text = 'Paragraph #{}'.format(i)
        para = Paragraph(text, styles['Normal'])
        flowables.append(para)
        flowables.append(spacer)

    doc.build(flowables)


if __name__ == '__main__':
    create_document()
