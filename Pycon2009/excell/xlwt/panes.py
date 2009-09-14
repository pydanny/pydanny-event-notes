from xlwt import Workbook
from xlwt.Utils import rowcol_to_cell

def setup_sheet(sheet):
    for col in range(20):
        for row in range(80):
            sheet.write(row,col,rowcol_to_cell(row,col))
    sheet.vert_split_pos = 2
    sheet.horz_split_pos = 10
    sheet.vert_split_first_visible = 5
    sheet.horz_split_first_visible = 40
    
w = Workbook()
ws = w.add_sheet('Split')
setup_sheet(ws)
ws = w.add_sheet('Freeze')
setup_sheet(ws)
ws.panes_frozen = True

w.save('panes.xls')
