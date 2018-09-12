"""www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'index/',view.hello),
    path(r'admin_list/',view.admin_list),
    path('demo/',view.demo),
    path(r'admin_role/', view.admin_role),
    path(r'admin_add/', view.admin_add),
    path(r'admin_edit/', view.admin_edit),
    path(r'admin_rule/', view.admin_rule),
    path('login/',view.login),
    path('regist/',view.regist),
    path('welcome/',view.welcome),
]
