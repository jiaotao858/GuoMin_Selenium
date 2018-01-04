# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from setting import *

#分别读取登录用户名和密码
class Ebooking_Login(unittest.TestCase):
    '''ebooking模拟登录流程'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        print("===用例开始执行===")

    def login_text(self):
        driver = self.driver
        driver.get(ebooking_url)
        driver.maximize_window()
        for i in range(1, len(lir)):
            us_locator = '//*[@id="loginId"]'
            ps_locator = '//*[@id="password"]'
            ent_locator = '/html/body/div[1]/div[2]/div/div/div[1]/button'
            toast_class = 'layui-layer-content'
            error_class = 'error-tips'
            driver.find_element(By.XPATH, us_locator).clear()
            driver.find_element(By.XPATH, ps_locator).clear()
            driver.find_element(By.XPATH, us_locator).send_keys(lir[i][1])
            driver.find_element(By.XPATH, ps_locator).send_keys(lir[i][2])
            driver.find_element(By.XPATH, ent_locator).click()
            time.sleep(3)
            try:
                assert driver.find_element(By.CLASS_NAME, error_class).text != None
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
        print("===用例执行结果===")




