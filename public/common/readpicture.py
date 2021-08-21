#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : readpicture.py
# @Author: shuiU
# @Date  : 2019/5/28
# @Desc  :
import base64

from public.common.pathUtils import picturePath


def readPicture(path):
    with open(path,'rb') as f:
        context =  base64.b64encode(f.read())
        print(context)
        f.close()

readPicture(picturePath)