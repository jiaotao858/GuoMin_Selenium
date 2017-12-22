#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from setting import *


class Order_Refund(unittest.TestCase):
    '''账户退单操作'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        print("===用例开始执行===")

    def hotel_refund(self):
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
        print("默认支付方式：账户支付")
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div[6]/div[2]/label[1]").click()
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
        driver.find_element_by_xpath("//*[@id='layui-layer3']/div[3]/a[2]").click()
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
        h_ord_sta = driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div[3]/div[1]/button").text
        assert h_ord_sta == "确认支付"
        driver.find_element_by_xpath("/html/body/div[3]/div/form/div/div[3]/div[1]/button").click()
        driver.implicitly_wait(10)
        h_ord_suss = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]").text
        assert h_ord_suss == "支付成功"
        driver.save_screenshot(filename + "账户付款成功.png")
        driver.find_element_by_link_text("查看订单").click()
        driver.implicitly_wait(10)
        h_pay_suss = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div").text
        self.assertEqual(h_pay_suss, "订单信息", "订单详情查看失败！")
        driver.save_screenshot(filename + "账户支付-订单详情.png")
        print("hotel订单付款成功！")

        """hote系统退单操作"""
        # driver.find_element_by_xpath("/html/body/div[1]/div/ul/li[1]/a/div/a[1]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/ul/li[1]/a").click()
        driver.find_element_by_link_text("酒店订单").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/div[2]/div[1]/input").send_keys(billId)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/div[3]/button").click()
        time.sleep(3)
        #根据预留房和非预留房执行方式
        refund_status = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/table/tbody/tr[1]/td[9]").text
        if refund_status == "已确认":
            driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div/div/div/table/tbody/tr[1]/td[10]/a[3]/div").click()
            print("订单类型-预留房")
        elif refund_status == "待确认":
            driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/table/tbody/tr[1]/td[10]/a[2]/div").click()
            print("订单类型-非预留房")
        else:
            driver.quit()
            print("退单操作执行不成功")
        #确认申请退单
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[2]/button[2]").click()
        driver.refresh()
        driver.implicitly_wait(10)
        refund_status_sec = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/table/tbody/tr[1]/td[9]").text
        self.assertEqual(refund_status_sec,"（退款中）已确认","退款状态不正确")
        driver.save_screenshot(filename+"订单退款中.png")
        print("hotel申请退款成功！")

        """admin系统确认同意退单"""
        driver.switch_to.window(handles[1])
        driver.find_element_by_link_text("退款订单").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div[1]/input[1]").send_keys(billId)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div[1]/input[3]").click()
        driver.implicitly_wait(10)
        locator = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/table/tbody/tr/td[1]").text
        self.assertEqual(locator,billId,"查询退单失败！")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/table/tbody/tr[1]/td[10]/a[1]").click()
        driver.implicitly_wait(10)
        driver.find_element_by_class_name('layui-layer-btn1').click()
        # driver.execute_script("document.getElementsByClassName('layui-layer-btn1')[0].click()")
        time.sleep(3)
        print("退款提示内容： "+driver.find_element_by_class_name('layui-layer-content').text)
        driver.find_element_by_link_text("订单查询").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[1]/input").send_keys(billId)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[3]/input").click()
        driver.refresh()
        time.sleep(5)
        driver.refresh()
        driver.implicitly_wait(10)
        a_ord_sta1 = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/table/tbody/tr[2]/td[5]/span").text
        self.assertEqual(a_ord_sta1,"已退款","退单处理失败，请查看！")
        time.sleep(3)
        driver.refresh()
        driver.save_screenshot(filename+"订单退款成功.png")
        print("admin同意退单成功！----》前台申请退款成功！")

    def tearDown(self):
        self.driver.quit()
        print("====用例执行结果====")


