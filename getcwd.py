#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : getcwd.py
# @Author: shuiU
# @Date  : 2019/4/11
# @Desc  :

import os
def get_cwd():
    path =os.path.dirname(os.path.abspath(__file__))
    return path