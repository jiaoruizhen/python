#!D:\PyCharm 2018.2.2\python\python
# -*- coding: UTF-8 -*-
from bottle import default_app, get, run
from beaker.middleware import SessionMiddleware
from com.dognessnetwork.web.usercontroller import *
# 设置session参数
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': '/tmp/sessions/simple',
    'session.auto': True
}
# 函数主入口
if __name__ == '__main__':
    app_argv = SessionMiddleware(default_app(), session_opts)
    run(app=app_argv, host='0.0.0.0', port=8000, debug=True, reloader=True)