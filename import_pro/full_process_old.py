#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from setting import *


class FullProcess(unittest.TestCase):
    """模拟完成下单入住流程"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        print("===用例开始执行===")

    def test_full_process(self):

        """hotel系统购买操作"""
        driver = self.driver
        driver.get(hotel_url)
        driver.execute_script("window.open('" + admin_url +"')")
        driver.execute_script("window.open('" + ebooking_url + "')")
        handles = driver.window_handles
        driver.switch_to.window(handles[0])
        driver.maximize_window()
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input').send_keys(hotel_id)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input').send_keys(hotel_pwd)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/div/a').click()
        driver.implicitly_wait(10)
        login_h = driver.find_element_by_xpath("/html/body/div[2]/div/div/span[2]").text
        self.assertEqual(login_h, login_hotel_a, "hotel账户登录不正确！")
        driver.save_screenshot(filename + "登录hote系统成功.png")
        driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[1]/input').clear()
        driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[1]/input').send_keys(prov_name)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[4]/input').send_keys(hotel_name)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/form/div[5]/button').click()
        driver.execute_script("window.scrollTo(1000,1000)")
        # 点击预定按钮
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div[11]/a').click()
        # 填写入住人信息
        driver.implicitly_wait(30)
        driver.find_element_by_xpath('/html/body/div[3]/div/form/div[3]/ul/li[1]/div/input').send_keys(buyer_name)
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div[3]/ul/li[2]/div/input").send_keys(buyer_mobile)
        # 选择支付方式(账户支付)
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div[6]/div[2]/label[1]").click()
        # 提交订单
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div[6]/div[3]/button").click()
        # 获取订单编号
        billNO = str(driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div[2]/div/div[1]/div[2]").text)
        billId = billNO.split("：")[1]
        driver.save_screenshot(filename + "获取订单编号.png")
        print("获取订单编号成功，订单编号： "+billId)
        print ("hotel下单操作成功！")

        """admin系统确认操作"""
        driver.switch_to.window(handles[2])
        driver.find_element_by_name("loginId").send_keys(admin_id)
        driver.find_element_by_name("password").send_keys(admin_pwd)
        driver.find_element_by_id("loginBtn").click()
        driver.implicitly_wait(10)
        login_admin = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/h3/a").text
        self.assertEqual(login_admin, login_admin_a, "admin账户登录不正确！")
        driver.save_screenshot(filename + "登录admin系统成功.png")
        # 点击订单查询
        driver.implicitly_wait(10)
        driver.find_element_by_link_text("订单查询").click()
        # 搜索订单
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[1]/input").send_keys(billId)
        # 确认订单
        driver.find_element_by_link_text("查看").click()
        driver.find_element_by_link_text("确认hold房").click()
        # 确认hold房
        driver.implicitly_wait(5)
        # driver.find_element_by_xpath("//*[@id='layui-layer3']/div[3]/a[2]").click()
        #临时测试用元素修改
        driver.find_element_by_xpath("//*[@id='layui-layer2']/div[3]/a[2]").click()
        time.sleep(3)
        driver.refresh()
        # 验证状态
        a_ord_sta = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/table[1]/tbody/tr[8]/td[2]/a").text
        assert a_ord_sta == "取消hold房"
        driver.save_screenshot(filename + "hold房成功.png")
        print ("admin确认订单成功！")

        """切换回hote系统进行付款操作"""
        driver.switch_to.window(handles[0])
        driver.refresh()
        h_ord_sta = driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div[3]/div[1]/button").text
        assert h_ord_sta == "确认支付"
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div[3]/div[1]/button").click()
        driver.implicitly_wait(10)
        h_ord_suss = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]").text
        assert h_ord_suss == "支付成功"
        driver.save_screenshot(filename+"订单付款成功.png")
        print ("hotel订单付款成功！")

        """ebooking系统进行入住操作"""
        driver.switch_to.window(handles[1])
        driver.find_element_by_xpath("//*[@id='loginId']").send_keys(ebooking_id)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(ebooking_pwd)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/button").click()
        login_e = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/span").text
        self.assertEqual(login_e,login_ebooking_a,"ebooking账号登录不正确！")
        driver.save_screenshot(filename+"登录ebooking系统成功.png")
        driver.find_element_by_link_text("订单处理").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/div[2]/input").send_keys(billId)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/form/div[2]/button[1]").click()
        driver.implicitly_wait(10)
        driver.find_element_by_link_text("处理").click()
        driver.implicitly_wait(10)
        driver.find_element_by_link_text("确认订单").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='layui-layer100002']/div[2]/div/div/input").send_keys('1233')
        driver.find_element_by_xpath("//*[@id='layui-layer100002']/div[3]/a").click()
        time.sleep(2)
        # print(driver.find_element_by_class_name('layui-layer-content').text)
        print ("ebooking客人入住成功！")

    def tearDown(self):
        self.driver.quit()
        print("===用例执行结果===")


