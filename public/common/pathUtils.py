#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : pathUtils.py
# @Author: shuiU
# @Date  : 2019/4/10
# @Desc  :

import os

# 获取项目中所需要路径的目录地址
#页面定位对象xml 运行app的配置 读取测试案例的地址
rootPath = os.path.dirname(os.path.abspath('..'))
pageElementPath = rootPath+'/config/magfine.xml'
appConfigPath = rootPath+'/config/connect.ini'
testCasePath = rootPath+'/testcase/appTestCase.xlsx'
picturePath = rootPath+'/testcase/testphonexiugaia.jpg'