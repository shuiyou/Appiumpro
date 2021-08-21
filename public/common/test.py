#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: shuiU
# @Date  : 2019/4/26
# @Desc  :

import unittest
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common import actions

from public.common.basepage import BasePage
from public.common.elementOperation import elementOperate
from appium.webdriver import WebElement, webdriver


class Mydemo(unittest.TestCase):

    def testa(self):
        bp =BasePage('http://localhost:4723/wd/hub','desired_cap')
        op =elementOperate(bp)
        elementOne =op.findAppElement('数字A')
        elementOne.send_keys(1)
        elementTwo =op.findAppElement('数字B')
        elementTwo.send_keys(2)
        elementThree = op.findAppElement('运算加号')
        elementThree.click()
        elementfour=op.findAppElement('滑动按钮')
        op.moveSipeButton()
        result = op.findAppElement('结果').text
        print(result)


if __name__=='__main__':
        unittest.main()
        suite = unittest.TestSuite('testa')