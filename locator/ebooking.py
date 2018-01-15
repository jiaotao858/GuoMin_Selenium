#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 登录页元素
EBOOKING_LOGIN_USER = "//*[@id='loginId']"  # 登录框用户名
EBOOKING_LOGIN_PASSWORD = "//*[@id='password']"  # 登录框密码
EBOOKING_LOGIN_BUTTON = "/html/body/div[1]/div[2]/div/div/div[1]/button"  # 登录页登录按钮

# 首页元素
EBOOKING_INDEX_SURE = "/html/body/div[1]/div[1]/div/div/span"   # 验证登录是否成功

# 订单处理页元素
EBOOKING_BILL_INPUT = "/html/body/div[1]/div[3]/div[1]/form/div[2]/input"  # 输入订单编号框
EBOOKING_BILL_SEARCH = "/html/body/div[1]/div[3]/div[1]/form/div[2]/button[1]"  # 【查询】按钮

# 酒店确认
EBOOKING_SUREN_NO = "//*[@id='layui-layer100002']/div[2]/div/div/input"  # 酒店确认号输入框
EBOOKING_SUREN_BUTTON = "//*[@id='layui-layer100002']/div[3]/a"   # 确认号【确认】按钮

