from xlsxwriter.utility import (
    xl_rowcol_to_cell, xl_cell_to_rowcol,
    xl_col_to_name, xl_range, xl_range_abs)

cell = xl_rowcol_to_cell(1, 2)  # C2
print(cell)

print(xl_rowcol_to_cell(0, 0))  # A1
print(xl_rowcol_to_cell(0, 1))   # B1
print(xl_rowcol_to_cell(1, 0))   # A2

print(xl_rowcol_to_cell(0, 0, col_abs=True))                # $A1
print(xl_rowcol_to_cell(0, 0, row_abs=True))                # A$1
print(xl_rowcol_to_cell(0, 0, row_abs=True, col_abs=True))  # $A$1


(row, col) = xl_cell_to_rowcol('A1')  # (0, 0)
(row, col) = xl_cell_to_rowcol('B1')  # (0, 1)
(row, col) = xl_cell_to_rowcol('C2')  # (1, 2)
(row, col) = xl_cell_to_rowcol('$C2')  # (1, 2)
(row, col) = xl_cell_to_rowcol('C$2')  # (1, 2)
(row, col) = xl_cell_to_rowcol('$C$2')  # (1, 2)

column = xl_col_to_name(0)  # A
column = xl_col_to_name(1)  # B
column = xl_col_to_name(702)  # AAA

column = xl_col_to_name(0, False)  # A
column = xl_col_to_name(0, True)  # $A
column = xl_col_to_name(1, True)  # $B

cell_range = xl_range(0, 0, 9, 0)  # A1:A10
cell_range = xl_range(1, 2, 8, 2)  # C2:C9
cell_range = xl_range(0, 0, 3, 4)  # A1:E4

cell_range = xl_range_abs(0, 0, 9, 0)  # $A$1:$A$10
cell_range = xl_range_abs(1, 2, 8, 2)  # $C$2:$C$9
cell_range = xl_range_abs(0, 0, 3, 4)  # $A$1:$E$4
