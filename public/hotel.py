# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from locator.hotel import *
from locator.admin import *
from setting import *

"""
hotel 公共方法包含
1.hotel登录
2.首页购买
3.获取订单编号
4.hotel登出
"""


def hotel_login(driver):
    driver.find_element(By.XPATH, HOTEL_LOGIN_USER).send_keys(hotel_id)
    driver.find_element(By.XPATH, HOTEL_LOGIN_PASSWORD).send_keys(hotel_pwd)
    driver.find_element(By.XPATH, HOTEL_LOGIN_BUTTON).click()
    driver.implicitly_wait(10)


def hotel_buy(driver):
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
    print("获取订单编号成功，订单编号： " + billId)
    print("hotel下单操作成功！")