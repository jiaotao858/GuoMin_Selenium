# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from setting import *
from demo.read_excel import *

def error_login():
    driver = webdriver.Chrome()
    driver.get(hotel_url)
    driver.maximize_window()
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input').send_keys(a[0])
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input').send_keys(str(list[1]))
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/div/a').click()
    driver.implicitly_wait(10)
    msg_list = []
    msg = driver.find_element_by_class_name('layui-layer-content').text
    msg_list.append(msg)
    print(msg_list)

def read():
    a = read_exc()
    print(a[3])


if __name__ == '__main__':
    # read_excel()
    # error_login()
    read()