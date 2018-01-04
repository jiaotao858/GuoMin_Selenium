# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv,execjs
from setting import *

liw = []
def login_t():
    driver = webdriver.Chrome()
    driver.get(hotel_url)
    # driver.maximize_window()
    us_locator = '/html/body/div/div[2]/form/div[1]/input'
    ps_locator = '/html/body/div/div[2]/form/div[2]/input'
    ent_locator = '/html/body/div/div[2]/form/div[4]/div/a'
    toast_locator = 'layui-layer-content'

    driver.find_element(By.XPATH,us_locator).clear()
    driver.find_element(By.XPATH,ps_locator).clear()
    driver.find_element(By.XPATH,us_locator).send_keys('')
    driver.find_element(By.XPATH,ps_locator).send_keys('')
    driver.find_element(By.XPATH,ent_locator).click()
    time.sleep(2)

    try:
        assert driver.find_element(By.CLASS_NAME, 'layui-layer-title').text == '信息'
        msg = driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[2]').text
        print(msg)
        liw.append(msg)
        driver.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a').click()
    except:
        err_msg = driver.find_element(By.CLASS_NAME, toast_locator).text
        print(err_msg)
        # liw.append(err_msg)
    # a = driver.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[2]').text
    # print(a)
    # driver.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a').click()

    # js = 'var q = document.getElementsByClassName("layui-layer-btn0")[0].click();'
    # driver.execute_script(js)

csvFile_w = open('..\login_error_xxxxxxxxx.csv', 'wb')
write_csv = csv.writer(csvFile_w)
write_csv.writerow('11111111111')
csvFile_w.close()

if __name__ == '__main__':
    # read_csv()
    login_t()
    print(liw)

