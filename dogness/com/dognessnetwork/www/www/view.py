#!D:\PyCharm 2018.2.2\python\python
# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return render(request, 'index.html')

def admin_list(request):
    return render(request, 'admin/admin-list.html')

def admin_add(request):
    return render(request, 'admin/admin-add.html')

def admin_role(request):
    return render(request, 'admin/admin-role.html')

def admin_edit(request):
    return render(request, 'admin/admin-edit.html')

def admin_rule(request):
    return render(request, 'admin/admin-rule.html')

def welcome(request):
    return render(request,"welcome.html")

def login(request):
    return render(request,"login.html")

def regist(request):
    return render(request,"regist.html")

def demo(request):
    return render(request,'demo.html')