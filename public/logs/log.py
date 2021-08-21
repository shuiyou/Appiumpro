#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : log.py
# @Author: shuiU
# @Date  : 2019/4/11
# @Desc  :


import logging
import os
import time

import getcwd


def get_log(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.info())

    #设置日志存放的路径，日志名称

    currentDate =time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    path = getcwd.get_cwd
    #设置错误日志和全日志目录
    all_log_path = os.path.join(path, 'Logs/All_Logs/')
    all_error_path = os.path.join(path,'Logs/ERROT_Logs')