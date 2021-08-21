#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ExcelParseUtils.py
# @Author: shuiU
# @Date  : 2019/4/30
# @Desc  :

import pandas as pd
from public.common.pathUtils import testCasePath

testCaseRows =1
caseParmKeyRow =1
addIndex =2
caseParmKeyList =[]     #参数list
NeedExcuteList = []     #需要执行的测试案例号
loatorList=[]           #提供给webdriver定位的参数


class Excelparsing:

    # def readExcel(self,sheetName):
    #     loatorList = []  # 提供给webdriver定位的参数
    #     data=xlrd.open_workbook(testCasePath,encoding_override='utf-8')
    #     worksheet = data.sheet_by_name(sheetName)
    #     realRows =worksheet.nrows
    #     RealCols =worksheet.ncols
    #
    #     caseParmKeyList = self.getParameterkey(realRows,worksheet)
    #     NeedExcuteList =self.getRealExcuteCase(worksheet)
    #     length = caseParmKeyList.__len__()
    #     for casenum in NeedExcuteList:
    #         dict = {}
    #         casedata = worksheet.row_values(int(casenum)+1)
    #         i = 0
    #         while i<length-1:
    #             dict[caseParmKeyList[i]]=casedata[i]
    #             i+=1
    #         print(dict)
    #         loatorList.append(dict)
    #     return  loatorList

    def readExcel(self,sheetName):
        df = pd.read_excel(testCasePath,sheet_name=sheetName)
        return  df

    #获取测试案例的参数
    # def getParameterkey(self,colnums,worksheet):
    #     datas =worksheet.row_values(caseParmKeyRow)
    #     list =[]
    #     for data in datas:
    #         list.append(data)
    #     return list

    #获取测试用例
    def getCaseinfo(self,sheetName,needRunCase):
        """
        :param sheetName
        :type str
        :param needRunCase
        :type list
        :rtype: list
        """
        data = self.readExcel(sheetName)
        print(data)
        dataHead = data.head(0)
        print(dataHead)
        data2 =data.iloc[[0,2]]
        print(data2)
        alltestCase =list(data2.T.to_dict().values())
        print(alltestCase)
        runtestCase =[]
        for i in needRunCase:
            runtestCase.append(alltestCase[i-1])
        print(runtestCase)
        return runtestCase

    #获取执行的测试用例
    def getRealExcuteCase(self,worksheet):
        casenums = worksheet.cell_value(0,1)
        caselist =str(casenums).split(',')
        return caselist

    # @staticmethod
    # def getCaseinfo(sheetname):
    #     p = Excelparsing()
    #     CaseInfoList = p.readExcel(sheetname)
    #     return CaseInfoList




    #检查cell里面的内容是不是Str，如果不是设置为Str
    # 说明：ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    @staticmethod
    def vaildCellType(cell):
        if cell.ctype!=1:
            cell.ctype=1
            print('设置Cell单元格格式为String成功')
        else:
            pass



    




if __name__ == '__main__':
    p = Excelparsing()
    a =[1,2]
    data = p.getCaseinfo('Sheet1',a)

