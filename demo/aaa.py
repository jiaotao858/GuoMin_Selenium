# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
<<<<<<< HEAD
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
=======
import csv,execjs
from setting import *

li = []
fobj = open('..\login_error.csv', 'r+')
read_vsv = csv.reader(fobj)
for resd_line in read_vsv:
    li.append(resd_line)
print(li)
>>>>>>> 3b49f62a103470524ef0cdd2fff628f6ea3df409


def login_t():
    driver = webdriver.Chrome()
    driver.get(hotel_url)
    # driver.maximize_window()
<<<<<<< HEAD
    for i in range(1, len(lir)):
=======
    for i in range(1, len(li)):
>>>>>>> 3b49f62a103470524ef0cdd2fff628f6ea3df409
        us_locator = '/html/body/div/div[2]/form/div[1]/input'
        ps_locator = '/html/body/div/div[2]/form/div[2]/input'
        ent_locator = '/html/body/div/div[2]/form/div[4]/div/a'
        toast_locator = 'layui-layer-content'
<<<<<<< HEAD
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
=======
        driver.find_element(By.XPATH,us_locator).clear()
        driver.find_element(By.XPATH,ps_locator).clear()
        driver.find_element(By.XPATH,us_locator).send_keys(li[i][1])
        driver.find_element(By.XPATH,ps_locator).send_keys(li[i][2])
        driver.find_element(By.XPATH,ent_locator).click()
        time.sleep(3)
        try:
            assert driver.find_element(By.CLASS_NAME, 'layui-layer-title').text == '信息'
>>>>>>> 3b49f62a103470524ef0cdd2fff628f6ea3df409
            js = 'var q = document.getElementsByClassName("layui-layer-btn0")[0].click();'
            driver.execute_script(js)
        except:
            err_msg = driver.find_element(By.CLASS_NAME, toast_locator).text
            print(err_msg)
<<<<<<< HEAD
            liw.append(err_msg)
=======
>>>>>>> 3b49f62a103470524ef0cdd2fff628f6ea3df409

if __name__ == '__main__':
    # read_csv()
    login_t()
<<<<<<< HEAD
    print(liw)
=======
>>>>>>> 3b49f62a103470524ef0cdd2fff628f6ea3df409
