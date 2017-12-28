# -*- coding:utf-8 -*-
import xlrd
import xlwt

def read_exc():
    workbook = xlrd.open_workbook(r'..\error_login.xls')
    # print(workbook.sheet_names())
    # gm_hotel = workbook.sheet_by_index(0)
    gm_hotel = workbook.sheet_by_name('国民酒店')
    list1 = []
    for i in range(2,gm_hotel.nrows):
        for j in range (1,3):
            list1.append(gm_hotel.cell(i,j).value)
    return list1

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
    print(read_exc())

