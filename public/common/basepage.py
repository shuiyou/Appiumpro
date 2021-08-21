#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : basepage.py
# @Author: shuiU
# @Date  : 2019/3/14
# @Desc  :
import configparser

from appium import webdriver
from flask import json

from public.common.pathUtils import appConfigPath


def getDevice(deviceName):
    config = configparser.ConfigParser()
    config.read(appConfigPath)
    realapp = config.get('app',deviceName)
    realapp_dict = json.loads(realapp)
    return  realapp_dict


class BasePage():

    def __init__(self,url,deviceName):
        self.desired_cap =getDevice(deviceName)
        self.driver = webdriver.Remote(url,self.desired_cap)


    def getDriver(self):
        return self.driver


    #安转app


    #检查app运行状态
    def queryAppstatus(self):
        statusnum =self.driver.query_app_state()
        if statusnum ==0:
            print('当前app状态未知')
        elif statusnum==1:
            print('app没有运行')
        elif statusnum==2:
            print('app正常后台运行')
        elif statusnum==3:
            print('app处于悬挂待机状态')
        elif statusnum ==4:
            print('app为当前运行状态')
        else:
            print('未知状态')

    #让app后台运行
    def appMoveBackground(self,second=10):
        self.driver.background_app(second)

    #让app从后台激活
    def appActive(self,app_id):
        self.driver.activate_app(app_id)





    def close(self):
        self.driver.quit()






