# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from setting import *
import csv

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
    driver.maximize_window()
    for i in range(1, len(li)):
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input').clear()
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input').clear()
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input').send_keys(li[i][1])
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input').send_keys(li[i][2])
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/div/a').click()
        time.sleep(2)
        if driver.find_element_by_xpath('/html/body/div[1]/div[2]/h2').text == '会员登录':
            print("登陆失败！")
            if driver.find_element_by_class_name('layui-layer-content').text is not None:
                print(driver.find_element_by_class_name('layui-layer-content').text)
            if driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[3]/a').text == '确定':
                driver.find_element_by_xpath('//*[@id="layui-layer3"]/div[3]/a').click()
        else:
            print("66666666666666666")

if __name__ == '__main__':
    # read_csv()
    login_t()


# driver = webdriver.Chrome()
#     driver.get(hotel_url)
#     driver.maximize_window()
#     driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input').send_keys(a[0])
#     driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input').send_keys(str(list[1]))
#     driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/div/a').click()