#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 首页元素
ADMIN_INDEX_ASSERT = "/html/body/div[1]/div[1]/div[1]/div/div[2]/h3/a"    # 当前登录用户，判断登录是否成功

# 订单查询页元素
ADMIN_BILL_SEARCH = "/html/body/div[1]/div[2]/div/div/div[2]/div[1]/input"  # 订单编号框
ADMIN_BILL_BUTTON = "/html/body/div[1]/div[2]/div/div/div[2]/div[3]/input"  # 查询按钮
ADMIN_BILL_STATUS = "/html/body/div[1]/div[3]/form/div[2]/table/tbody/tr[2]/td[5]/span"  # 订单状态
ADMIN_BILL_REFUND = "/html/body/div[1]/div[3]/form/div[2]/table/tbody/tr[2]/td[6]/a[2]"  # 退单按钮

# 退款订单页元素
ADMIN_BILL_REFUND_BILLNO = "/html/body/div[1]/div/div[2]/form/div[1]/input[1]"  # 订单编号输入框
ADMIN_BILL_REFUND_SEARCH = "/html/body/div[1]/div/div[2]/form/div[1]/input[3]"  # 搜索按钮
ADMIN_BILL_REFUND_SUREID = "/html/body/div[1]/div/div[3]/table/tbody/tr/td[1]"    # 确认订单编号
ADMIN_BILL_REFUND_AGREE = "/html/body/div[1]/div/div[3]/table/tbody/tr[1]/td[10]/a[1]"    # 同意退单按钮
ADMIN_BILL_REFUND_SECONDAGREE = "layui-layer-btn1"    # 退款二次确认


# 确认HOLD房页元素
ADMIN_HOLD_SURE = "//*[@id='layui-layer2']/div[3]/a[2]"  # 确认hold房按钮
ADMIN_HOLD_SURE_SECOND = "/html/body/div[1]/div/div[2]/table[1]/tbody/tr[8]/td[2]/a"  # 确认hold是否成功

ADMIN_SECONDAGREE = "layui-layer-btn1"  # 二次确认




