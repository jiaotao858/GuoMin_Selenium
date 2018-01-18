import unittest
from import_pro import full_process, order_pay, order_refund
from hotel_test import hotel_login
from ebooking_test import ebooking_login


def suite():
    suitetest = unittest.TestSuite()
    suitetest.addTest(full_process.FullProcess('test_full_process'))
    print("<现在执行下单用例集合>")
    return suitetest


def suite1():
    suitetest1 = unittest.TestSuite()
    suitetest1.addTest(order_pay.OrderPay('pay_account'))
    suitetest1.addTest(order_pay.OrderPay('pay_weixin'))
    suitetest1.addTest(order_pay.OrderPay('pay_zhifubao'))
    print("<现在执行支付方式用例集合>")
    return suitetest1


def suite2():
    suitetest2 = unittest.TestSuite()
    suitetest2.addTest(order_refund.OrderRefund('hotel_refund'))
    print("<现在执行退款用例集合>")
    return suitetest2


def suite3():
    suitetest3 = unittest.TestSuite()
    suitetest3.addTest(hotel_login.Hotel_Login('login_text'))
    # suitetest3.addTest(ebooking_login.Ebooking_Login('login_text'))
    print("<现在执行登录用例集合>")
    return suitetest3


# def allsuite():
    # allTest = unittest.TextTestResult(suite1(),suite2())
    # print("suite1,suit2 执行")
    # return AllSuite
    # pass


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite1())