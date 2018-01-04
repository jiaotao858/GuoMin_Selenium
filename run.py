import unittest
from import_pro import full_process,order_pay,order_refund
from hotel_test import hotel_login
from ebooking_test import ebooking_login

def suite1():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(full_process.Full_Process('test_full_process'))
    print("<现在执行下单用例集合>")
    return suiteTest

def suite2():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(order_pay.Order_Pay('pay_account'))
    suiteTest.addTest(order_pay.Order_Pay('pay_weixin'))
    suiteTest.addTest(order_pay.Order_Pay('pay_zhifubao'))
    print("<现在执行支付方式用例集合>")
    return suiteTest

def suite3():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(order_refund.Order_Refund('hotel_refund'))
    print("<现在执行退款用例集合>")
    return suiteTest

def suite4():
    suiteTest = unittest.TestSuite()
    # suiteTest.addTest(hotel_login.Hotel_Login('login_text'))
    suiteTest.addTest(ebooking_login.Ebooking_Login('login_text'))
    print("<现在执行登录用例集合>")
    return suiteTest

def AllSuite():
    # allTest = unittest.TextTestResult(suite1(),suite2())
    # print("suite1,suit2 执行")
    # return AllSuite
    pass


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite4())