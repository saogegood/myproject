"""
Module/Script Name:<urls>
Author: <Devin>
Date: <2023/3/27 9:41>
Description: <Description of Module/Script>
"""
from django.urls import path
from . import views

urlpatterns = [
    # 定义根路由，当访问根目录时调用 views 模块中的 hello 函数
    path('', views.hello, name='hello'),
]