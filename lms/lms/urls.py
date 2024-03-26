"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.contrib import admin
from app01 import views

urlpatterns = [
    # 管理员账户登陆
    re_path(r'^admin/', admin.site.urls),
    # 出版社列表
    re_path(r'^publisher_list/', views.publisher_list),
    re_path(r'^add_publisher/', views.add_publisher),
    re_path(r'^drop_publisher/', views.drop_publisher),
    re_path(r'^edit_publisher/', views.edit_publisher),
    re_path(r'^book_list/', views.book_list),
    re_path(r'^add_book/', views.add_book),
    re_path(r'^drop_book/', views.drop_book),
    re_path(r'^edit_book/', views.edit_book),
    re_path(r'^author_list/', views.author_list),
    re_path(r'^add_author/', views.add_author),
    re_path(r'^drop_author/', views.drop_author),
    re_path(r'^edit_author/', views.edit_author),
    re_path(r'^$', views.publisher_list),
]
