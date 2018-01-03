# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv,execjs
from setting import *


# def read_csv():
li = []
fobj = open('..\login_error.csv', 'r+')
read_vsv = csv.reader(fobj)
for resd_line in read_vsv:
    li.append(resd_line)
print(li)


def login_t():
    driver = webdriver.Chrome()
    driver.get(hotel_url)
    # driver.maximize_window()
    for i in range(1, len(li)):
        us_locator = '/html/body/div/div[2]/form/div[1]/input'
        ps_locator = '/html/body/div/div[2]/form/div[2]/input'
        ent_locator = '/html/body/div/div[2]/form/div[4]/div/a'
        toast_locator = 'layui-layer-content'
        # err_locator = '//*[@id="layui-layer13"]/div[2]'
        # yes_locator1 ='//*[@id="layui-layer3"]/div[3]/a'
        # yes_locator ='layui-layer-shade3'
        # yes_locator ='账号或密码错误'
        driver.find_element(By.XPATH,us_locator).clear()
        driver.find_element(By.XPATH,ps_locator).clear()
        driver.find_element(By.XPATH,us_locator).send_keys(li[i][1])
        driver.find_element(By.XPATH,ps_locator).send_keys(li[i][2])
        driver.find_element(By.XPATH,ent_locator).click()
        time.sleep(2)
        try:
            WebDriverWait(driver,5,0.5).until(EC.text_to_be_present_in_element(By.CLASS_NAME,'layui-layer-title'),'信息')
            js = 'var q = document.getElementsByClassName("layui-layer-btn0")[0].click();'
            driver.execute_script(js)
            print("11111111")
        except:
            print(driver.find_element(By.CLASS_NAME,toast_locator).text)
        # finally:
        #     driver.quit()

if __name__ == '__main__':
    # read_csv()
    login_t()


# driver = webdriver.Chrome()
#     driver.get(hotel_url)
#     driver.maximize_window()
#     driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input').send_keys(a[0])
#     driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input').send_keys(str(list[1]))
#     driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/div/a').click()