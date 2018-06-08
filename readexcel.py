import openpyxl as xl

wb = xl.load_workbook('sample.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
value = sheet.cell(row=1, column=2).value
print(value)
