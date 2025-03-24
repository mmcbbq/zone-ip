import openpyxl

path = 'Mappe1.xlsx'

wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active

max_col = sheet_obj.max_column
max_row = sheet_obj.max_row
ip= 10
teil = []
for j in range(2, max_row + 1):
    sub = sheet_obj.cell(row=j,column=1).value[0:2]+sheet_obj.cell(row=j,column=2).value[0]
    c = 1
    while sub in teil:
        sub= sheet_obj.cell(row=j,column=1).value[0+1:2+1]+sheet_obj.cell(row=j,column=2).value[0]
        c += 1
    teil.append(sub)

    print(f'Teil: {sheet_obj.cell(row=j, column=1).value} {sheet_obj.cell(row=j, column=2).value}')
    print(f"Domainname={sub}.linux.zz")
    print(f'Netzwerk eth0 192.168.{ip}.0 /24' )
    print(f'Netzwerk eth1 10.101.207.{ip+100} /24 \n\n\n' )

    ip+= 5
print(teil)
