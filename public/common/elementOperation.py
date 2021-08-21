#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : elementOperation.py
# @Author: shuiU
# @Date  : 2019/3/14
# @Desc  :
from appium.webdriver.common.touch_action import TouchAction
from public.common.basepage import BasePage
from public.common.parseXMLutils import parseXmlUtils

class elementOperate():
    def __init__(self,ob):
        self.webdriver =BasePage.getDriver(ob)


    def allways_allow(self):
        pass

    def findAppElement(self,locatorName):
        p = parseXmlUtils()
        currentElement = p.getPageElementInfo(locatorName)
        #等待1000毫秒
        # self.webdriver.implicitly_wait(1000)
        try:
            if(currentElement):
                type =currentElement['type']
                value =currentElement['value']
                if(type=='id'):
                    element =self.webdriver.find_element_by_id(value)
                elif(type=='name'):
                    element =self.webdriver.find_element_by_name(value)
                elif (type == 'xpath'):
                    element =self.webdriver.find_element_by_xpath(value)
                elif(type=='accessiblileity'):
                    element =self.webdriver.find_element_by_accessibility_id(value)
                elif(type=='ccsSelector'):
                    element =self.webdriver.find_element_by_css_selector(value)
                elif(type=='image'):
                    element=self.webdriver.find_element_by_image(value)
                elif (type == 'className'):
                    element = self.webdriver.find_elements_by_class_name(value)
                else:
                    print('不存在这种定位方式')
                WebElement =element
                return WebElement
        except BaseException:
                print('未找到当前页面元素')


    def moveSipeButton(self):
        action = TouchAction(self.webdriver)
        action.press(x=174,y=396)
        action.move_to(x=226,y=393)
        print(type(action))
        action.perform()


    def waitTime(self,time):
        self.webdriver.implicitly_wait(time)

    def PageTimeout(self,time):
        pass



