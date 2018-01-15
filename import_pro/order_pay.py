#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from setting import *
from selenium.webdriver.common.by import By
from locator.hotel import *
from locator.admin import *
from locator.ebooking import *


class OrderPay(unittest.TestCase):
    """测试订单不同支付方式"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        print("===用例开始执行===")

    def pay_account(self):

        """hotel系统购买操作"""
        driver = self.driver
        driver.get(hotel_url)
        driver.execute_script("window.open('" + admin_url +"')")
        handles = driver.window_handles
        driver.maximize_window()
        driver.find_element(By.XPATH, HOTEL_LOGIN_USER).send_keys(hotel_id)
        driver.find_element(By.XPATH, HOTEL_LOGIN_PASSWORD).send_keys(hotel_pwd)
        driver.find_element(By.XPATH, HOTEL_LOGIN_BUTTON).click()
        driver.implicitly_wait(10)
        login_h = driver.find_element(By.XPATH, HOTEL_INDEX_ASSERT).text
        self.assertEqual(login_h, login_hotel_a, "hotel账户登录不正确！")
        driver.save_screenshot(filename + "登录hote系统成功.png")
        driver.find_element(By.XPATH, HOTEL_INDEX_PROV).clear()
        driver.find_element(By.XPATH, HOTEL_INDEX_PROV).send_keys(prov_name)
        driver.find_element(By.XPATH, HOTEL_INDEX_HOTEL).send_keys(hotel_name)
        driver.find_element(By.XPATH, HOTEL_INDEX_SEARCH_BUTTON).click()
        # 点击预定按钮
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, HOTEL_ORDER).click()
        driver.implicitly_wait(30)
        driver.find_element(By.XPATH, HOTEL_BUYER_NAME).send_keys(buyer_name)
        driver.find_element(By.XPATH, HOTEL_BUYER_MOBIL).send_keys(buyer_mobile)
        print("选择支付方式：账户支付")
        driver.find_element(By.XPATH, HOTEL_BUYER_PAY_TYPE_ACCOUNT).click()
        # 提交订单
        driver.find_element(By.XPATH, HOTEL_BUYER_SUBMIT).click()
        billNO = str(driver.find_element(By.XPATH, HOTEL_PAY_BILLID).text)
        billId = billNO.split("：")[1]
        driver.save_screenshot(filename + "获取订单编号.png")
        print("获取订单编号成功，订单编号： "+billId)
        print ("hotel下单操作成功！")

        """admin系统确认操作"""
        driver.switch_to.window(handles[1])
        driver.find_element_by_name("loginId").send_keys(admin_id)
        driver.find_element_by_name("password").send_keys(admin_pwd)
        driver.find_element_by_id("loginBtn").click()
        driver.implicitly_wait(10)
        login_admin = driver.find_element(By.XPATH, ADMIN_INDEX_ASSERT).text
        self.assertEqual(login_admin, login_admin_a, "admin账户登录不正确！")
        driver.save_screenshot(filename + "登录admin系统成功.png")
        # 点击订单查询
        driver.implicitly_wait(10)
        driver.find_element(By.LINK_TEXT, "订单查询").click()
        # 搜索订单
        driver.find_element(By.XPATH, ADMIN_BILL_SEARCH).send_keys(billId)
        # 确认订单
        driver.find_element(By.LINK_TEXT, "查看").click()
        driver.find_element(By.LINK_TEXT, "确认hold房").click()
        # 确认hold房
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, ADMIN_HOLD_SURE).click()
        time.sleep(3)
        driver.refresh()
        # 验证状态
        a_ord_sta = driver.find_element(By.XPATH, ADMIN_HOLD_SURE_SECOND).text
        assert a_ord_sta == "取消hold房"
        driver.save_screenshot(filename + "hold房成功.png")
        print("admin确认订单成功！")

        """切换回hote系统进行付款操作"""
        driver.switch_to.window(handles[0])
        driver.refresh()
        h_ord_sta = driver.find_element(By.XPATH, HOTEL_PAY_BUTTON).text
        assert h_ord_sta == "确认支付"
        driver.find_element(By.XPATH, HOTEL_PAY_BUTTON).click()
        driver.implicitly_wait(10)
        h_ord_suss = driver.find_element(By.XPATH, HOTEL_PAY_SURE).text
        assert h_ord_suss == "支付成功"
        driver.save_screenshot(filename + "账户付款成功.png")
        driver.find_element_by_link_text("查看订单").click()
        driver.implicitly_wait(10)
        h_pay_suss = driver.find_element(By.XPATH, HOTEL_DETAILS_TITLE).text
        self.assertEqual(h_pay_suss, "订单信息", "订单详情查看失败！")
        driver.save_screenshot(filename + "账户支付-订单详情.png")
        print("hotel订单付款成功！")

    def pay_weixin(self):

        """hotel系统购买操作"""
        driver = self.driver
        driver.get(hotel_url)
        driver.execute_script("window.open('" + admin_url +"')")
        handles = driver.window_handles
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
        # 点击预定按钮
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div[11]/a').click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath('/html/body/div[3]/div/form/div[3]/ul/li[1]/div/input').send_keys(buyer_name)
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div[3]/ul/li[2]/div/input").send_keys(buyer_mobile)
        print("选择支付方式：微信")
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div[6]/div[2]/label[3]").click()
        # 提交订单
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div[6]/div[3]/button").click()
        billNO = str(driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div[2]/div/div[1]/div[2]").text)
        billId = billNO.split("：")[1]
        driver.save_screenshot(filename + "获取订单编号.png")
        print("获取订单编号成功，订单编号： "+billId)
        print ("hotel下单操作成功！")

        """admin系统确认操作"""
        driver.switch_to.window(handles[1])
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
        # 临时测试用元素修改
        driver.find_element_by_xpath("//*[@id='layui-layer2']/div[3]/a[2]").click()
        time.sleep(3)
        driver.refresh()
        # 验证状态
        a_ord_sta = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/table[1]/tbody/tr[8]/td[2]/a").text
        assert a_ord_sta == "取消hold房"
        driver.save_screenshot(filename + "hold房成功.png")
        print("admin确认订单成功！")

        """切换回hote系统进行付款操作"""
        driver.switch_to.window(handles[0])
        driver.refresh()
        #等待微信扫码
        driver.implicitly_wait(360)
        h_ord_suss = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]").text
        assert h_ord_suss == "支付成功"
        driver.save_screenshot(filename + "微信付款成功.png")
        driver.find_element_by_link_text("查看订单").click()
        driver.implicitly_wait(10)
        h_pay_suss = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div").text
        self.assertEqual(h_pay_suss,"订单信息","订单详情查看失败！")
        driver.save_screenshot(filename+"微信支付-订单详情.png")
        print("hotel订单付款成功！")

    def pay_zhifubao(self):

        """hotel系统购买操作"""
        driver = self.driver
        driver.get(hotel_url)
        driver.execute_script("window.open('" + admin_url +"')")
        handles = driver.window_handles
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
        # 点击预定按钮
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div[11]/a').click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath('/html/body/div[3]/div/form/div[3]/ul/li[1]/div/input').send_keys(buyer_name)
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div[3]/ul/li[2]/div/input").send_keys(buyer_mobile)
        print("选择支付方式：支付宝")
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div[6]/div[2]/label[2]").click()
        # 提交订单
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div[6]/div[3]/button").click()
        billNO = str(driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div[2]/div/div[1]/div[2]").text)
        billId = billNO.split("：")[1]
        driver.save_screenshot(filename + "获取订单编号.png")
        print("获取订单编号成功，订单编号： "+billId)
        print ("hotel下单操作成功！")

        """admin系统确认操作"""
        driver.switch_to.window(handles[1])
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
        # 临时测试用元素修改
        driver.find_element_by_xpath("//*[@id='layui-layer2']/div[3]/a[2]").click()
        time.sleep(3)
        driver.refresh()
        # 验证状态
        a_ord_sta = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/table[1]/tbody/tr[8]/td[2]/a").text
        assert a_ord_sta == "取消hold房"
        driver.save_screenshot(filename + "hold房成功.png")
        print("admin确认订单成功！")

        """切换回hote系统进行付款操作"""
        driver.switch_to.window(handles[0])
        driver.refresh()
        #等待支付宝扫码
        driver.implicitly_wait(360)
        h_ord_suss = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]").text
        assert h_ord_suss == "支付成功"
        driver.save_screenshot(filename + "支付宝付款成功.png")
        driver.find_element_by_link_text("查看订单").click()
        driver.implicitly_wait(10)
        h_pay_suss = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div").text
        self.assertEqual(h_pay_suss,"订单信息","订单详情查看失败！")
        driver.save_screenshot(filename+"支付宝支付-订单详情.png")
        print("hotel订单付款成功！")

    def tearDown(self):
        self.driver.quit()
        print("用例执行结束...")


