import openpyxl

path = 'Mappe1.xlsx'

wb_obj = openpyxl.load_workbook(path)
sheet = wb_obj.active

# sheet_obj = wb_obj.active

max_col = sheet.max_column
max_row = sheet.max_row
ip = 10

for x in range(2,max_row):
    print(f'\t\t\t\t- to {sheet.cell(row=x, column=4).value}')
    print(f'\t\t\t\t\tvia {sheet.cell(row=x, column=5).value}')
    print()