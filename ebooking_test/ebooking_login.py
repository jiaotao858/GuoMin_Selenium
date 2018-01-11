# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from setting import *


class Ebooking_Login(unittest.TestCase):
    """admin模拟登录流程,次用例未完成，查找弹窗失败"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("===用例开始执行===")

    def login_text(self):
        driver = self.driver
        driver.get(admin_url)
        driver.maximize_window()
        for i in range(1, len(lir)):
            toast_class = 'layui-layer-content'
            error_class = 'error-tips'
            driver.find_element(By.NAME, 'loginId').clear()
            driver.find_element(By.NAME, 'password').clear()
            driver.find_element(By.NAME, 'loginId').send_keys(lir[i][1])
            driver.find_element(By.NAME, 'password').send_keys(lir[i][2])
            driver.find_element(By.ID, 'loginBtn').click()
            time.sleep(3)
            try:
                msg = driver.find_element(By.CLASS_NAME, error_class).text
                assert msg is None
                msg = driver.find_element(By.CLASS_NAME, error_class).text
                print(msg)
                liw.append(msg)
            except:
                err_msg = driver.find_element(By.CLASS_NAME, toast_class).text
                print(err_msg)
                liw.append(err_msg)
        driver.quit()

    def tearDown(self):
        self.driver.quit()
        print("===用例执行结束===")




