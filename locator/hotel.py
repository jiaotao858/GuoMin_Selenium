#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 登录页元素
HOTEL_LOGIN_USER = "/html/body/div/div[2]/form/div[1]/input"   # 登录框用户名
HOTEL_LOGIN_PASSWORD = "/html/body/div/div[2]/form/div[2]/input"   # 登录框密码
HOTEL_LOGIN_BUTTON = "/html/body/div/div[2]/form/div[4]/div/a"   # 登录按钮

# 首页元素
HOTEL_INDEX_PROV = "/html/body/div[3]/div/div[1]/div[2]/form/div[1]/input"  # 首页省份
HOTEL_INDEX_HOTEL = "/html/body/div[3]/div/div[1]/div[2]/form/div[4]/input"  # 首页酒店名称
HOTEL_INDEX_SEARCH_BUTTON = "/html/body/div[3]/div/div[1]/div[2]/form/div[5]/button"  # 首页搜索按钮
HOTEL_INDEX_ASSERT = "/html/body/div[2]/div/div/span[2]"    # 当前登录用户，判断登录是否成功
HOTEL_INDEX_BILL_MANAGE = "/html/body/div[1]/div/ul/li[1]/a"    # 首页订单管理按钮

# 酒店列表页元素
HOTEL_ORDER = "/html/body/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div[11]/a"    # 酒店列表下单按钮

# 下单页元素
HOTEL_BUYER_NAME = "/html/body/div[3]/div/form/div[3]/ul/li[1]/div/input"    # 下单人姓名
HOTEL_BUYER_MOBIL = "/html/body/div[3]/div/form/div[3]/ul/li[2]/div/input"   # 下单人联系电话
HOTEL_BUYER_PAY_TYPE_ACCOUNT = "/html/body/div[3]/div/form/div[6]/div[2]/label[1]"   # 选择支付方式-账户支付
HOTEL_BUYER_PAY_TYPE_ZFB = "/html/body/div[3]/div/form/div[6]/div[2]/label[2]"   # 选择支付方式-支付宝支付
HOTEL_BUYER_PAY_TYPE_WX = "/html/body/div[3]/div/form/div[6]/div[2]/label[3]"   # 选择支付方式-微信支付
HOTEL_BUYER_SUBMIT = "/html/body/div[3]/div/form/div[6]/div[3]/button"   # 提交订单

# 支付页元素
HOTEL_PAY_BILLID = "/html/body/div[3]/div/form/div/div[2]/div/div[1]/div[2]"   # 获取订单编号
HOTEL_PAY_BUTTON = "/html/body/div[3]/div/form/div/div[3]/div[1]/button"   # 支付按钮名称
HOTEL_PAY_SURE = "/html/body/div[3]/div/div/div/div[1]"   # 验证是否支付

# 订单详情页
HOTEL_DETAILS_TITLE = "/html/body/div[3]/div/div[1]/div"   # 订单详情页标题

# 订单查询页
HOTEL_BILL_MANAGE_BILLNO = "/html/body/div[3]/div[1]/form/div[2]/div[1]/input"  # 订单管理页订单编号框
HOTEL_BILL_MANAGE_BUTTON = "/html/body/div[3]/div[1]/form/div[3]/button"  # 订单管理页查询按钮
HOTEL_BILL_MANAGE_STATUS = "/html/body/div[3]/div[2]/div/div/div/table/tbody/tr[1]/td[9]"  # 订单管理页订单状态（预留房/非预留房）
HOTEL_BILL_MANAGE_CLROOM = "/html/body/div[3]/div[2]/div/div/div/table/tbody/tr[1]/td[10]/a[3]/div"     # 预留房点击按钮
HOTEL_BILL_MANAGE_OPROOM = "/html/body/div[3]/div[2]/div/div/div/table/tbody/tr[1]/td[10]/a[2]/div"     # 非预留房点击按钮
HOTEL_BILL_MANAGE_SURERE = ""




