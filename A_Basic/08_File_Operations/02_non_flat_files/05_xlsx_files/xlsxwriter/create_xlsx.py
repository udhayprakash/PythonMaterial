import os

import xlsxwriter

file_path = str(os.path.abspath(os.path.join(os.path.expanduser('~'), 'Desktop')))
excel_path = file_path + os.sep + 'my_excel_file.xlsx'
print "excel path", excel_path

workbook = xlsxwriter.Workbook(excel_path)
worksheet1 = workbook.add_worksheet('Report')
header_format = workbook.add_format(
    {'bold': True, 'align': 'center', 'valign': 'vcenter', 'fg_color': '#D7E4BC', 'border': 1})
center_format = workbook.add_format({'align': 'center'})
left_format = workbook.add_format({'align': 'left'})
Thank_format = workbook.add_format(
    {'align': 'left', 'bold': True, 'valign': 'vcenter', 'font_size': 13, 'border': 0})
Detail_format = workbook.add_format(
    {'align': 'left', 'bold': True, 'valign': 'vcenter', 'font_size': 11, 'border': 0})
merge_format = workbook.add_format(
    {'bold': True, 'border': 0, 'align': 'center', 'valign': 'vcenter', 'font_size': 18, 'font_color': 'red', })
worksheet1.freeze_panes(9, 9)
worksheet1.set_column('A:D', 50)
worksheet1.set_row(10, 20)
worksheet1.set_selection('E9')
worksheet1.set_tab_color('red')
worksheet1.set_column(0, 0, 9)
worksheet1.set_column(1, 1, 100)
worksheet1.set_column(2, 2, 25)
worksheet1.set_column(3, 3, 20)
worksheet1.set_column(4, 4, 25)
headr = ['Sr.no.', 'Name', 'Email', 'Mobile', 'city']
worksheet1.merge_range('B1:B2', 'Report', merge_format)
worksheet1.write(3, 1, "Name- UdhayPrakash", Detail_format)
worksheet1.write(4, 1, "Email address- example@gmail.com", Detail_format)
worksheet1.write(5, 1, "mobile- 5464449464", Detail_format)
worksheet1.write(6, 1, "city- abc", Detail_format)
# Some text to demonstrate scrolling.
for col in range(0, 5):
    worksheet1.write(8, col, headr[col], header_format)

points = [
    os.environ['USERPROFILE'] + os.sep + 'Desktop/python-docx/docx.py',
    os.environ['USERPROFILE'] + os.sep + 'Desktop/python-docx/abc.py',
    'welcome to python docx',
    'welcome to my python blog',
]
for row in range(9, len(points) + 9):
    worksheet1.write(row, 0, row - 8, center_format)
    worksheet1.write(row, 1, points[row - 9], left_format)
    worksheet1.write(row, 2, 'example@gmail.com', center_format)
    worksheet1.write(row, 3, '45466464646', center_format)
    worksheet1.write(row, 4, 'abc', center_format)
    last = row

worksheet1.write(last + 4, 1, "Thanks & Regards", Thank_format)
worksheet1.write(last + 5, 1, "UdhayPrakash")
worksheet1.insert_image('B' + str(last + 7),
                        os.environ['USERPROFILE'] + os.sep + r'Pictures/UdhayPrakashPethakamsetty.jpg')
workbook.close()
