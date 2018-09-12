#!D:\PyCharm 2018.2.2\python\python
# -*- coding: UTF-8 -*-
from bottle import *

class HTTPResponse(Response, BottleException):
    def __init__(self, body='', status=None, headers=None, **more_headers):
        super(HTTPResponse, self).__init__(body, status, headers, **more_headers)

    def apply(self, response):
        response._status_code = self._status_code
        response._status_line = self._status_line
        #重写此对象并修改为下面判断代码，将设置的请求头放进来
        if self._headers:
            if response._headers:
                response._headers.update(self._headers)
            else:
                response._headers = self._headers

        response._cookies = self._cookies
        response.body = self.body