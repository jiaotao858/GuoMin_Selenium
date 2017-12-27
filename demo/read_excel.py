# -*- coding:utf-8 -*-
import xlrd
import xlwt

def read_excel():
    workbook = xlrd.open_workbook(r'..\read_excel.xlsx')
    print(workbook.sheet_names())

    sheet2 = workbook.sheet_by_index(0)
    # sheet2 = workbook.sheet_by_name('Sheet1')

    print(sheet2.name,sheet2.nrows,sheet2.ncols)

    rows = sheet2.row_values(0)
    cols = sheet2.col_values(0)
    print(rows)
    print(cols)
    print(sheet2.cell(0,0).value)
    print(sheet2.cell_value(0,0))
    print(sheet2.row(0)[0].value)
    print(sheet2.cell(0,0).ctype)

def wrilt_excel():
    f = xlwt.Workbook()

    sheet =f.add_sheet('测试一下',cell_overwrite_ok=True)
    rows = ['1','2','3','4']
    cols = ['a','b','c','d']
    status = ['买入','卖出']

    for i in range(0,len(rows)):
        sheet.write(0,i,rows[i])
    for j in range(0,len(cols)):
        sheet.write(j+1,1,cols[j])

    f.save('..\demo1.xls')

if __name__ == '__main__':
    wrilt_excel()

