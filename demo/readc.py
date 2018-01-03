#encoding=utf-8
import sys,os
import csv
list = []
def a():
    fobj = open('..\login_error.csv','r+')
    read_vsv = csv.reader(fobj)
    for resd_line in read_vsv:
        list.append(resd_line)
    print(list)
        # fobj.close()

if __name__ == '__main__':
    a()
