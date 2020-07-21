#!/usr/bin/python
"""
Purpose: Working with sub-elements in html
"""

from lxml import etree

html = etree.Element("html")
etree.SubElement(html, "head").text = "Head of HTML"
etree.SubElement(html, "title").text = "I am the title!"
etree.SubElement(html, "body").text = "Here is the body"

print(etree.tostring(html, pretty_print=True).decode('utf-8'))

