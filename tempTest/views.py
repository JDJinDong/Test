#encoding:utf-8
from django.shortcuts import render,HttpResponse

# Create your views here.
#定义一个类属性和方法
class TestTemp(object):
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex

	def show(self):
		return "%s的年龄是:%s,性别是:%s"%(self.name,self.age,self.sex)


def showClass(request):
	# 实例化类对象
	temp = TestTemp("张丰广","18","男吧?")
	# 把所有的变量全部加载到内存里，可能会造成浪费
	#return render(request,"tempTest/index.html",locals())
	cont = {"temp":temp}
	return render(request,"tempTest/index.html",context=cont)

def filterTest(request):
	testList = ["abc","hello","world"]
	return render(request,"tempTest/index.html",{"contList":testList})

def forloopTest(request):
	contList = [1,2,3,4,5]
	return render(request,"tempTest/forloop.html")



