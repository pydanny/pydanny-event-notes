from xlwt import Utils

print Utils.col_by_name('AA')
print Utils.col_by_name('A')

print Utils.cell_to_rowcol('A1')
print Utils.cell_to_rowcol('$A$1')

print Utils.cell_to_rowcol2('A1')

print Utils.rowcol_to_cell(0,0)
print Utils.rowcol_to_cell(0,0,False,True)
print Utils.rowcol_to_cell(
    row=0,col=0,row_abs=True,col_abs=True
    )

print Utils.cellrange_to_rowcol_pair('1:3')
print Utils.cellrange_to_rowcol_pair('B:G')
print Utils.cellrange_to_rowcol_pair('A2:B7')
print Utils.cellrange_to_rowcol_pair('A1')

print Utils.valid_sheet_name('')
print Utils.valid_sheet_name("'quoted'")
print Utils.valid_sheet_name("O'hare")
print Utils.valid_sheet_name("X"*32)
print Utils.valid_sheet_name("[]:\\?/*\x00")
