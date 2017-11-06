#encoding:utf-8
from django import template


#第一种注册方法
# register = template.Library()

#自定义的注册方法
# def percrent(value):
# 	return str(value) + "%"
# #注册
# register.filter(percrent)


#第二种注册方式
register = template.Library()
@register.filter(name="percrent")
def percrent(value):
	return str(value) + "%"
#注册
register.filter(percrent)

