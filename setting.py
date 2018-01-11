#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time,os,csv

# 设置图片保存路径
localday = time.strftime("%Y-%m-%d", time.localtime())
localtime = time.strftime("%Y-%m-%d %H%M%S", time.localtime())
# filename = "C:\\Users\\allonshore\\Desktop\\text\\" + localday + "\\" + localtime + "\\"
filename = "C:\\Users\\jiaotao\\Desktop" + localday + "\\"+localtime+"\\"
if os.path.exists(filename) is False:
    os.makedirs(filename)

# 读取hotel登录账号
# lir = []
# liw = []
# 读取csv中用户名和密码
# csvFile_r = open('login_error.csv', 'r+')
# read_vsv = csv.reader(csvFile_r)
# for resd_line in read_vsv:
#     lir.append(resd_line)
# print(lir)
# csvFile_r.close()

# 写入hotel登录账号
# 将提示结果写入csv中
# csvFile_w = open('..\login_error.csv', 'a+')
# write_csv = csv.reader(csvFile_w)
# write_csv.readrow
# csvFile_w.close()
# for w in range(len(liw)):
#     print(liw[w])

# test_hotel系统信息
# hotel_url = "https://testhotel.guomintrip.com"
# hotel_id = "18640857881"
# hotel_pwd = "jt123456"
# login_hotel_a = "中共中央旅行社 - 焦涛"
# hotel_name = "迪士尼欢乐酒店"
# prov_name = "贵州省"
# buyer_name = "正常流程"
# buyer_mobile = "18640857881"

# hotel线上系统
# HOTEL_URL = "https://hotel.guomintrip.com"
# hotel_id = "18640857881"
# hotel_pwd = "jt123456"
# hotel_name = "迪士尼欢乐酒店"
# prov_name = "贵州省"
# buyer_name = ""
# buyer_mobile = ""

# 唐山test_hotel测试系统
hotel_url = "http://testhotel.hblckj.cn"
hotel_id = "18640857881"
hotel_pwd = "jt123456"
login_hotel_a = "中共中央旅行社 - 焦涛"
hotel_name = "迪士尼欢乐酒店"
prov_name = "贵州省"
buyer_name = "正常流程"
buyer_mobile = "18640857881"

# test_admin系统信息
# admin_url = "https://testadmin.guomintrip.com"
# admin_id = "guo"
# admin_pwd ="gm666qwe"
# login_admin_a = "guo"

# admin线上系统
# admin_url = "https://admin.guomintrip.com"
# admin_id = "guo"
# admin_pwd ="gm666qwe"

# 唐山test_admin系统信息
admin_url = "https://testadmin.hblckj.cn"
admin_id = "guo"
admin_pwd ="ts123456"
login_admin_a = "guo"

# test_ebooking系统信息
# ebooking_url = "https://testebooking.guomintrip.com"
# ebooking_id = "15524638915"
# ebooking_pwd ="jt123456"
# login_ebooking_a = "迪士尼欢乐酒店"

# ebooking线上系统
# ebooking_url = "https://ebooking.guomintrip.com"
# ebooking_id = "15524638915"
# ebooking_pwd ="jt123456"

# test_ebooking系统信息
ebooking_url = "https://testebooking.hblckj.cn"
ebooking_id = "15524638915"
ebooking_pwd ="jt123456"
login_ebooking_a = "迪士尼欢乐酒店"