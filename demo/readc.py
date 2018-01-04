#encoding=utf-8
import sys,os
import csv
list = []
# def a():
#     fobj = open('..\login_error.csv','r+')
#     read_vsv = csv.reader(fobj)
#     for resd_line in read_vsv:
#         list.append(resd_line)
#     print(list)
#         # fobj.close()

# csvFile_w = open('..\login_error_xxxxxxxxx.csv', 'a+')
# write_csv = csv.writer(csvFile_w)
# write_csv.writerow('hello','dff')
# csvFile_w.close()

# csvFile_r = open('..\login_error_xxxxxxxxx.csv', 'r+')
# read_csv = csv.reader(csvFile_r)
# for i in read_csv:
#     print(i)
# csvFile_r.close

fileHeader = ['name','score']
d1 = ['焦生',100]
d2 = ['王生',10]
csvFile = open('..\login_error_xxxxxxxxx.csv','a+',newline='')
write = csv.writer(csvFile)
write.writerow(fileHeader)
write.writerow(d1)
write.writerow(d2)
csvFile.close()

# csvFile1 = open('..\login_error_xxxxxxxxx.csv','r')
# dict_reader = csv.DictReader(csvFile1)
# for row in dict_reader:
#     print(row)