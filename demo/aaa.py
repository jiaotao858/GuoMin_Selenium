# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
from setting import *

lir = []
csvFile1 = open('..\login_error.csv', 'r+')
read_vsv = csv.reader(csvFile1)
for resd_line in read_vsv:
    lir.append(resd_line)
print(lir)

liw = []
# csvFile2 = open('..\login_error.csv', 'r+')
# read_vsv = csv.reader(csvFile1)
# for resd_line in read_vsv:
#     li.append(resd_line)


def login_t():
    driver = webdriver.Chrome()
    driver.get(hotel_url)
    # driver.maximize_window()
    for i in range(1, len(lir)):
        us_locator = '/html/body/div/div[2]/form/div[1]/input'
        ps_locator = '/html/body/div/div[2]/form/div[2]/input'
        ent_locator = '/html/body/div/div[2]/form/div[4]/div/a'
        toast_locator = 'layui-layer-content'
        driver.find_element(By.XPATH, us_locator).clear()
        driver.find_element(By.XPATH, ps_locator).clear()
        driver.find_element(By.XPATH, us_locator).send_keys(lir[i][1])
        driver.find_element(By.XPATH, ps_locator).send_keys(lir[i][2])
        driver.find_element(By.XPATH, ent_locator).click()
        time.sleep(3)
        try:
            assert driver.find_element(By.CLASS_NAME, 'layui-layer-title').text == '信息'
            js1 = 'document.getElementsByClassName("layui-layer-content")[0].innerHTML;'
            a = driver.execute_script(js1)
            print(a)
            js = 'var q = document.getElementsByClassName("layui-layer-btn0")[0].click();'
            driver.execute_script(js)
        except:
            err_msg = driver.find_element(By.CLASS_NAME, toast_locator).text
            print(err_msg)
            liw.append(err_msg)

if __name__ == '__main__':
    # read_csv()
    login_t()
    print(liw)
