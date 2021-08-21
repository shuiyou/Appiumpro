#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : parseXMLutils.py
# @Author: shuiU
# @Date  : 2019/4/10
# @Desc  :


import xml.etree.cElementTree as  ET
import os

class parseXmlUtils():

    def __init__(self):
        self.projectRootPath = os.path.dirname(os.path.abspath('..'))

    def getPageElementInfo(self,pageElementName):
        tree = ET.parse(self.projectRootPath+'/config/magfine.xml')
        root = tree.getroot()
        for locator in root.iter('locator'):
            if(pageElementName==locator.text):
                print(locator.get('type'))
                print(locator.get('value'))
                print(locator.attrib)
                return locator.attrib
            else:
                continue





if __name__ == '__main__':
    p = parseXmlUtils()
    pageelement ={}
    pageelement =p.getPageElementInfo(pageElementName='请选择')
    print(pageelement['type'])