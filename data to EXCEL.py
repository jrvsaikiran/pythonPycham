import openpyxl

path = "F:\Book1 - Copy.xlsx"

workbook = openpyxl.load_workbook(path)

sheet=workbook.active

for r in  range(1,6):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value="jrv sai kiran" #jrv will save in excel

workbook.save(path)





