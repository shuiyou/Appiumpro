#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dataPrivder.py
# @Author: shuiU
# @Date  : 2019/5/8
# @Desc  :



def data_provider(fn_data_provider,param=None):
    """
    Data provider decorator,
    allows another callable to provide the data for the test
    """
    def test_decorator(fn):
        def test_repl(self, *args):
            if hasattr(fn_data_provider, '__func__'):
                data = fn_data_provider.__func__()
            else:
                if param==None:
                    data = fn_data_provider()
                else:
                    data = fn_data_provider(param)

            for i in data:
                if (type(i).__name__=='dict'):
                    try:
                        fn(self, **i)
                    except AssertionError:
                        print("Assertion error caught with data set ", i)
                        raise
                else:
                    try:
                        fn(self, *i)
                    except AssertionError:
                        print("Assertion error caught with data set ", i)
                        raise
        return test_repl
    return test_decorator


