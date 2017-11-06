#encoding:utf-8
from django.conf.urls import url
from .views import showClass,filterTest,forloopTest

urlpatterns = [
    url(r'show', showClass),
	url(r"filter",filterTest),
	url(r"forloop",forloopTest), #循环计数


]
