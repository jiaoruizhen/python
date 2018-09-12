#!D:\PyCharm 2018.2.2\python\python
# -*- coding: UTF-8 -*-
class ReturnData:
    def __init__(self,code,msg):
        self.code=code
        self.msg=msg
    def __init__(self,code,msg,data):
        self.code = code
        self.msg = msg
        self.data=data
    def getReturnData(self):
        data={}
        data['code']=self.code
        data['msg']=self.msg
        data['data']=self.data
        return data

