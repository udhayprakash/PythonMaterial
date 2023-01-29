#!/usr/bin/env python
import os
import subprocess

import gtk
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Paragraph, SimpleDocTemplate


class form:
    # This is for wrap pdf text in pdf file

    def shrink_font_size(self, aW, aH, text, style):
        """Shrinks font size by using pdfmetrics to calculate the height
        of a paragraph, given the font name, size, and available width."""

        def break_lines(text, aW):
            # simpleSplit calculates how reportlab will break up the lines for
            # display in a paragraph, by using width/fontsize.
            return simpleSplit(text, style.fontName, style.fontSize, aW)

        def line_wrap(lines, style):
            # Get overall width of text by getting stringWidth of longest line
            width = stringWidth(max(lines), style.fontName, style.fontSize)
            # Paragraph height can be calculated via line spacing and number of
            # lines.
            height = style.leading * len(lines)
            return width, height

        lines = break_lines(text, aW)
        width, height = line_wrap(lines, style)

        while height > aH or width > aW:
            style.fontSize -= 1
            lines = break_lines(text, aW)
            width, height = line_wrap(lines, style)

    def __init__(self):
        # this is dialog box for choosing format and generate pdf file and docx
        # file text file xlx file etc....
        dialog = gtk.MessageDialog(
            None,
            gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
            gtk.MESSAGE_QUESTION,
            gtk.BUTTONS_OK_CANCEL,
            None,
        )
        dialog.set_position(gtk.WIN_POS_CENTER)
        dialog.set_markup("In which format you want to save")
        hbox = gtk.VBox()
        hbox.set_uposition(80, 60)
        entry = gtk.RadioButton(None, label="PDF")
        hbox.pack_end(entry)
        entry = gtk.RadioButton(entry, label="TXT")
        hbox.pack_end(entry)
        entry = gtk.RadioButton(entry, label="XLS")
        hbox.pack_end(entry)
        entry = gtk.RadioButton(entry, label="CSV")
        hbox.pack_end(entry)
        entry = gtk.RadioButton(entry, label="DOC")
        hbox.pack_end(entry)
        dialog.vbox.pack_end(hbox, True, True, 0)
        dialog.show_all()
        act = dialog.run()
        if act == -5:
            for r in entry.get_group():
                if r.get_active():
                    text = r.get_label().lower()
                    print(text)
            dialog.destroy()
            txt = "Lorem Ipsum is simply dummy text of the printing and type setting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            if text == "pdf":
                doc = SimpleDocTemplate(
                    os.path.join(os.path.expanduser("~"), "Desktop") + "\hello1.pdf"
                )
                parts = []
                PAGE_WIDTH, PAGE_HEIGHT = A4
                aW = PAGE_WIDTH - 1 * inch
                aH = PAGE_HEIGHT - 1 * inch
                style = ParagraphStyle(name="Times New Roman")
                style.fontSize = 12
                style.leading = 20
                self.shrink_font_size(aW, aH, txt, style)
                p = Paragraph(txt, style)
                style1 = ParagraphStyle(name="Times New Roman")
                style1.fontSize = 16
                style1.leading = 20
                style1.textColor = "red"
                style1.alignment = TA_CENTER
                q = Paragraph("Report", style1)
                parts.append(q)
                parts.append(p)
                doc.build(parts)
            else:
                file = open(
                    os.path.join(os.path.expanduser("~"), "Desktop") + "\hello1.pdf",
                    "wb",
                )
                file.write(txt)
                file.close()
            path_to_pdf = os.path.abspath(
                os.path.join(os.path.expanduser("~"), "Desktop") + "\hello1.pdf"
            )
            process = subprocess.Popen(
                [path_to_pdf],
                bufsize=2048,
                shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
            )
            process.wait()
        else:
            text = None
            dialog.destroy()

    def main(self):
        gtk.main()


if __name__ == "__main__":
    first = form()
    first.main()
