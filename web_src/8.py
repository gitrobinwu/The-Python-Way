#-*- coding:utf-8 -*- 
主题: 装饰器

# 面向切面编程
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。经常用于有切面需求的场景，比如: 插入日志,性能测试,事物处理,权限校验等场景.装饰器是解决这类问题的绝佳设计，有了装饰器，既可以抽离出大量与函数功能本身无关的雷同代码并继续重用。概括的讲,装饰器的作用就是为已经存在的对象添加额外的功能.

def foo():
	print 'I am foo'

def foo():
	print 'I am foo'
	logging.info("foo is running")

def use_logging(func):
	logging.warn('%s is running' %func.__name__)
	func()

def bar():
	print 'I am bar'

use_logging(bar)	

# 简单装饰器
import functools 
def use_logging(func):
	@functools.wraps(func)
	def wrapper(*args,**kwargs):
		logging.warn("%s in running" % func.__name__)
		return func(*args,**kwargs)
	return wrapper 	

def bar():
	print "I am bar"

bar = use_logging(bar)
bar() 

函数use_logging就是装饰器，它把执行真正业务方法的func包裹在函数里面
看起来像bar被use_logging装饰了.在这个例子中	,函数进入和退出时，被称为一个横切面(Aspect),这种编程方式被称为面向切面编程
@符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作.

def use_logging(func):
	def wrapper(*args,**kwargs):
		logging.warn('%s is running' % func.__name__)
		return func(*args)
	return wrapper 

@use_logging
def foo():
	print 'I am foo'

@use_logging
def bar():
	print 'I am bar'

装饰器在Python使用如此方便都要归因于Python的函数能像普通对象一样能作为参数传递给其他函数，可以被赋值给其他变量，可以作为返回值，可以被定义在另一个函数内.

# 带参数的装饰器
装饰器还有更大的灵活性，例如带参数的装饰器: 在上面装饰器唯一参数是执行业务的函数.
装饰器语法允许在调用时，提供其他参数，比如@decorator(a)
import functools 	
def use_logging(level):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kwargs):
			if level == 'warn':
				logging.warn("%s is running" % func.__name__)
			return func(*args)
		return wrapper 
	return decorator 

@use_logging(level="warn")
def foo(name="foo"):
	print "I am %s" % name 

foo() 

# 类装饰器
相比函数装饰器，类装饰器具有更大的灵活度，高内聚，封装性等有点。
使用类装饰器可以依靠内部的__call__方法，当使用@形式将装饰器附加到函数上时，就会调用此方法

class Foo(object):
	def __init__(self,func):
		self.__func = func

	def __call__(self):
		print 'class decorator running'
		self.__func()
		print 'class decorator ending'

@Foo
def bar():
	print 'bar'

bar() 

# functools.wraps
使用装饰器极大地复用了代码，但是也有一个缺点就是原函数的源信息不见了
from functools import wraps 
def logged(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		print func.__name__
		return func(*args,**kwargs)
	return with_logging

# 内置装饰器
@staticmethod @classmethod @property

@a
@b
@c
def f():pass
==> f = a(b(c(f)))

## 计算两个int和所用的时间
import time 
def add(a,b):
	init_time = time.time()
	sum_value = a+b
	print 'Time Elapsed: %s' % (time.time()-init_time)
	return sum_value
	
####
import time
def timeit(func):
	def wrapper(*args,**kwargs):
		init_time = time.time()
		value = func(*args,**kwargs)
		print 'Time Elasped %s:' % (time.time() - init_time)
		return value 
	return wrapper 

@timeit 
def add(a,b):
	return a+b 

###
@decorator 
def func(*args,**kwargs):
	return 

等价于
def func(*args,**kwargs):
	return 
func = decorator(func)

def time_unit(u):
	def timeit(func):
		def wrapper(a,b):
			init_time = time.time()
			value = func(a,b)
			print "Time is :%s" % (time.time() - init_time)
			return value 
		return wrapper
	return timeit

class calculations:
	@staticmethod
	@timeit_unit(IE6)
	def add(*nums):
		return sum(nums)

	@classmethod
	def multiply_int(cls,a,b):
		return cls.add(*(a*[b]))

##########################################################
# @property
将一个类方法变成类属性
举个例子，可以用@property做getter和setter
class candidate(object):
	def __init__(self):
		self._score = None

	@porperty 
	def score(self):
		return self._score 
	
	@score.settter 
	def score(self,val):
		if isinstance(val,(int,float)):
			if 0<= val <= 100:
				self._score = val 
			else:
				raise ValueError("the score has to be in the 0-100 range")
		else:
			raise TypeError("int and float type only")

	@score.deleter
	 def score(self):
		 self._score = None 

#  测试 		 
me = candidate()
print me.score
me.score = 70
pritt me.score 
me.score = 101 
	
class B(A):	
	def __init__(name,src): 
		super(B,self).__init__(name.src) 
	
@staticmethod @classmethod @property
# 属性函数property 
class Normal:
	def __init__(self):
		self.__x = None 
	
	@property
	def xx(self):
		print self.__x
		return self.__x 

	@xx.setter
	def xx(self,value):
		self.__x = value 
		print 'setx()'
	
	@xx.deleter
	def xx(self):
		print 'setx()'
		del self.__x

		


