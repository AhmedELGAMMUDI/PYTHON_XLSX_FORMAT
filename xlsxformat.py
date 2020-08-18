import xlsxwriter
workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 18)
titlecell = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'font_size':12,
        'valign': 'vcenter'})
worksheet.write('A1', 'Hello world',titlecell )

workbook.close()