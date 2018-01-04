# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from setting import *

driver = webdriver.Chrome()
driver.get(ebooking_url)
driver.maximize_window()
us_locator = '//*[@id="loginId"]'
ps_locator = '//*[@id="password"]'
ent_locator = '/html/body/div[1]/div[2]/div/div/div[1]/button'
toast_class = 'layui-layer-tips'
error_class = 'error-tips'

driver.find_element(By.XPATH, us_locator).clear()
driver.find_element(By.XPATH, ps_locator).clear()
driver.find_element(By.XPATH, us_locator).send_keys('')
driver.find_element(By.XPATH, ps_locator).send_keys('')
driver.find_element(By.XPATH, ent_locator).click()
time.sleep(3)
try:
    assert driver.find_element(By.CLASS_NAME, error_class).text != None
    msg = driver.find_element(By.CLASS_NAME, error_class).text
    print(msg)
except:
    err_msg = driver.find_element(By.CLASS_NAME, toast_class).text
    print(err_msg)
driver.quit()