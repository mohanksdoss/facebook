import openpyxl
book = openpyxl.load_workbook("D:\\Pythonexcel.xlsx")
sheet = book.active
cell = sheet.cell(row=2, column=2)
print(cell.value)

