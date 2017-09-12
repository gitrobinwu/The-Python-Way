#-*- coding:utf-8 -*- 
# 定义一个装饰器函数
def doc_func(func):
	#包裹函数(闭包)
	def warpfunc():
		# 做一些额外的事情
		print '%s called' % (func.__name__)
		func() 

	return warpfunc

@doc_func
def foo():
	print 'hello'

@doc_func
def bar():
	print 'nihao'

if __name__ == "__main__":
	foo() 

#-----------------------
class Student:
	'''学生类'''
	def __init__(self,name,age):
		'''构造函数init'''
		print '__init__...'
		self.name = name 
		self.age = age 

	def showMe(self):
		print self.name 
		print self.age 

	def __del__(self):
		'''析构函数'''
		print '__del__...'
	
if __name__== '__main__':
	s1 = Student('zhnag3',18)
	s1.showMe()

	s2 = Student("114",20)
	s2.showMe() 

class Student:
	# 如果一个变量，直接定义在类里面，而不是成员变量
	school = "itcast"
	def __init__(self,name,age):
		'''构造函数'''
		print "__init__..."
		self.name = name 
		self.__age == age 
		
	def showMe(self):
		'''普通成员方法'''
		print '''showMe()...'''
		print self.name 
		print self.__age 
		print Student.school 

	def getAge(self):
		return self.__age 

	def __del__(self):
		'''析构函数'''
		print '__del__...'

if __name__ == '__main__':
	s1 = Student("zhang3",18)
	s1.showMe()
	print s1.getAge()
	
	print "*"*20
	s2 = Student("114",20)
	s2.showMe()

	print "*"*20
	Student.school = "itheima"
	s1.showMe() 

class Student:
	# 静态成员变量
	age = 18
	def __init__(self,name,age):
		self.name = name 

	def showme(self):
		# 对象变量
		print self.name 
		print Student.age 

	@classmethod 
	def showme2(cls):
		print cls.age 

		
