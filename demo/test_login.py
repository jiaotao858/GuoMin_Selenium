import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting import *
import csv

list = []
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # WebDriverWait(driver)
        self.driver = webdriver.Chrome()
        self.driver.get(hotel_url)
        self.driver.maximize_window()

    def read_csv_test(self):
        fobj = open('..\login_error.csv', 'r+')
        read_vsv = csv.reader(fobj)
        for resd_line in read_vsv:
            list.append(resd_line)
        # print(list)


    def login_test(self):
        driver = self.driver
        for i in range(1,len(list)):

            driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input').send_keys(list[i][1])
            driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input').send_keys(list[i][2])
            driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/div/a').click()
            driver.implicitly_wait(10)
            if driver.find_element_by_xpath('/html/body/div[1]/div/ul/li[5]/a').text == '退出':
                driver.find_element_by_xpath('/html/body/div[1]/div/ul/li[5]/a').click()
            else:
                pass

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
