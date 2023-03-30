from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# 定义视图函数 hello，接收一个请求对象作为参数
def hello(request):
    # 返回一个 HTTP 响应对象，内容为 "Hello, World!"
    return HttpResponse("Hello world1234!")