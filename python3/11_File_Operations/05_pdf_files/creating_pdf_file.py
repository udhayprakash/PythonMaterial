#!/usr/bin/python
"""
Purpose: PDF file creation 

pip install pdfkit 
pip install wkhtmltopdf
Download wkhtmltopdf.exe from https://wkhtmltopdf.org/downloads.html
"""
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

path_wkthmltopdf = r'C:\Users\udhayPrakash\AppData\Local\Programs\Python\Python37\wkhtmltox-0.12.5-1.msvc2015-win64.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
pdfkit.from_url("http://google.com", "out.pdf", configuration=config)

# html_text = 'hello world'
# breakpoint()
# pdfkit.from_string(html_text, 'out.pdf', options=pdf_settings)
