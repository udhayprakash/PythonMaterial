import xlsxwriter

with xlsxwriter.Workbook("three.xlsx") as workbook:
    # By Default, the sheet names will be sheet1, sheet2, ...
    ws1 = workbook.add_worksheet()

    ws1.write("A1", "Hello")
    ws1.write_comment("A1", "This is a comment")
    ws1.write_comment("C3", "Hello", {"x_scale": 1.2, "y_scale": 0.8})
    ws1.write_comment("C3", "Atonement", {"author": "Elon Musk"})

    # author name can be defaultly specified
    ws1.set_comments_author("John Smith")

    ws1.write_comment("D3", "Hello", {"visible": False})

    workbook.add_worksheet("mysheet")
    worksheet = workbook.add_worksheet()

    text = "Formatted textbox"

    options = {
        "width": 256,
        "height": 100,
        "x_offset": 10,
        "y_offset": 10,
        "font": {"color": "red", "size": 14},
        "align": {"vertical": "middle", "horizontal": "center"},
        "gradient": {"colors": ["#DDEBCF", "#9CB86E", "#156B13"]},
    }

    worksheet.insert_textbox("B2", text, options)
    worksheet.insert_textbox("B9", "A simple textbox with some text")
    worksheet.insert_textbox("B10", "Line 1\nLine 2\n\nMore text")

    worksheet.insert_textbox("B12", "Some text", {"width": 256, "height": 100})

    worksheet.insert_textbox(
        "B14", "Size adjusted textbox", {"width": 288, "height": 30}
    )
    # or
    worksheet.insert_textbox(
        "B18", "Size adjusted textbox", {"x_scale": 1.5, "y_scale": 0.25}
    )

    # nesting format properties
    worksheet.insert_textbox(
        "B19",
        "Some text in a textbox with formatting",
        {
            "font": {"color": "white"},
            "align": {"vertical": "middle", "horizontal": "center"},
            "gradient": {"colors": ["green", "white"]},
        },
    )

    # borders to text box
    worksheet.insert_textbox(
        "B21", "A textbox with a color border", {"line": {"color": "#FF9900"}}
    )

    worksheet.insert_textbox(
        "B23", "A textbox with larger border", {"line": {"width": 3.25}}
    )

    worksheet.insert_textbox(
        "B27", "A textbox a dash border", {"line": {"dash_type": "dash_dot"}}
    )

    # workbook.close()
