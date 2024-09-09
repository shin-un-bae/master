import openpyxl

wb = openpyxl.load_workbook('db2_data.xlsx')
ws = wb.active

for row in ws.iter_rows():
    for col, cell in enumerate(row):
        print(f"{col}: {cell.value}")