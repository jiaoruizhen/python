#!D:\PyCharm 2018.2.2\python\python
# -*- coding: UTF-8 -*-
#前端调用
from bottle import *

from com.dognessnetwork.service.userService import *

from django.shortcuts import render_to_response
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

##解决跨域请求问题
@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

@get('/index')
def callback():
    return render_to_response("index.html")

@get('/findAll')
def findAll():
    return selectAll()