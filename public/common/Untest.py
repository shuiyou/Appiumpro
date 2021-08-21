#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Untest.py
# @Author: shuiU
# @Date  : 2019/5/7
# @Desc  :
import unittest

# from unittest_dataprovider import data_provider
from public.common.ExcelParseUtils import Excelparsing
from public.common.dataPrivder import data_provider


def func():
    list =[
        (1, 1, 2),
        (2, 2, 4),
        (3, 3, 6)
    ]
    return list

def func_1():
    list=[{'测试用例': '测试2+3', '数字A': '2.0', '数字B': '3.0', '预期结果': '5.0'},{'测试用例': '测试1+8', '数字C': '1.0', '数字D': '8.0', '预期结果': '9.0'}
    ]
    return list

def func_2():
    return Excelparsing.getCaseinfo(sheetname='Sheet1')


class CssParserTest(unittest.TestCase):


    nums = lambda:(
        (1, 1, 2),
        (2, 2, 4),
        (3, 3, 6)
    )

    staticmethod
    def add(number1,number2):
        return number1+number2

    @data_provider(func_2)
    def setUp(self,**dicts):
        print('测试开始')
        for key in dicts.keys():
            print(key)



    # def test_add(self,number1,number2,except_value):
    #         result = CssParserTest.add(number1,number2)
    #         self.assertEqual(result, except_value)
    def test(self):
        print('testing')

        # print(dicts)
        # print(dicts['测试用例'])



    def tearDown(self):
        print('测试结束')

if __name__=='__main__':
        unittest.main()







