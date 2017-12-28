import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from setting import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # WebDriverWait(driver)
        self.driver = webdriver.Chrome()
        self.driver.get(hotel_url)
        self.driver.maximize_window()


    def login(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/input').send_keys()
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/input').send_keys()
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/div/a').click()
        driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
