#!D:\PyCharm 2018.2.2\python\python
# -*- coding: UTF-8 -*-
#用户数据库操作
import pymysql
import sys
import json
from com.dognessnetwork.pojo.user import *
print(sys.getdefaultencoding())
db = pymysql.connect(host='192.168.0.188', port=3306, user='root', passwd='123456',db='test',charset='utf8')

consurs=db.cursor()
def findAll():
    try:
        db.ping(reconnect='true')
        consurs.execute('select * from user')
        results = consurs.fetchall()
        list=[]
        for i in results:
            list.append(i)
        return list
    except Exception as e:
        print(e)
        print("fetch data fail")
    finally:
        db.close()

def insert(user):
    sql = "INSERT INTO user(name, \
           username, age, sex, password) \
           VALUES ('%s', '%s', '%d', '%s', '%s' )" % \
          (user['name'], user['username'], user['age'], user['sex'], user['password'])
    try:
        db.ping(reconnect='true')
        consurs.execute(sql)
        db.commit()
        print('添加成功')
    except:
        db.rollback()
    finally:
        db.close()

def delet(user):
    sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)


