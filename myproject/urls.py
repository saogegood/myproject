"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin   # 引入Django自带的后台管理模块
from django.urls import path, include   # 引入Django的URL解析器path和include

urlpatterns = [
    # 引入 myapp 应用的路由配置，包括 myapp.urls 模块中的所有路由
    path('', include('myapp.urls')),  # 引入myapp应用的路由配置，其中''表示访问项目根路径时会调用myapp应用的路由配置
    path("admin/", admin.site.urls),   # 定义访问后台管理的路由规则，访问路径是 http://yourdomain.com/admin/

]

