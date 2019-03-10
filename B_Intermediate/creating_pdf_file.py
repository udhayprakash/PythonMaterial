import pdfkit

pdf_settings = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}
 

html_text = 'hello world'
pdfkit.from_html(html_text, 'out.pdf', options=pdf_settings)