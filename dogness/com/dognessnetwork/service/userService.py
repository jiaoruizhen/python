#!D:\PyCharm 2018.2.2\python\python
# -*- coding: UTF-8 -*-
#用户服务api
from com.dognessnetwork.dao.userDao import *
from com.dognessnetwork.pojo.user import *
from com.dognessnetwork.common.ReturnData import *
from django.http import HttpResponse
def selectAll():
    list = findAll()

    lists = []
    for i in list:
        users = user()
        users.setId(i[0])
        users.setName(i[1])
        users.setUsername(i[4])
        users.setPassword(i[2])
        users.setSex(i[3])
        users.setAge(i[5])
        lists.append(users.getUser())

    returndata1=ReturnData('0','成功',lists)

    return returndata1.getReturnData()