#!D:\PyCharm 2018.2.2\python\python
# -*- coding: UTF-8 -*-
class user:
    id=0;
    name='';
    username='';
    age=0
    password=''
    sex=''
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getUsername(self):
        return self.username
    def getPasswd(self):
        return self.password
    def getAge(self):
        return self.age
    def getSex(self):
        return self.sex

    def setName(self,name):
        user.name=name
    def setUsername(self,username):
        user.username=username
    def setPassword(self, password):
        user.password = password
    def setAge(self,age):
        user.age=age
    def setSex(self,sex):
        user.sex=sex
    def setId(self,id):
        user.id=id

    def getUser(self):
        data={}
        data['id']=self.id
        data['name']=self.name
        data['username']=self.username
        data['age']=self.age
        data['password']=self.password
        data['sex']=self.sex
        return data
