from selenium import webdriver
from selenium.webdriver.common.by import By
from locator.hotel import *
from locator.admin import *
from setting import *
from public.hotel import hotel_login, hotel_buy

"""
1.查看hote端该旅行社账户金额
2.通过该旅行社购买产品
3.在此查看该旅行社账户金额
"""


def admin():
    """hotel系统购买操作"""
    driver = webdriver.Chrome()
    driver.get(hotel_url)
    # driver.execute_script("window.open('" + admin_url + "')")
    driver.maximize_window()
    hotel_login(driver)

if __name__ == '__main__':
    admin()

