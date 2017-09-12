#-*- coding:utf-8 -*- 
主题: 异常，如何生成异常，异常处理，python对异常的支持，如何创建自定义异常，断言

1，检测和处理异常
检测和处理异常有两种主要形式: try-except和try-finally

2, try-except 语句
try: 
	try_sutie #watch for exceptions here 
except Exception[,reason]:
	except_suite #exception-handing code 

2, 带有多个except的try语句
def safe_float(obj):
	try:
		retval = flaot(obj)
	except ValueError:
		retval = 'could not convert non-number to float'
	except TypeError:
		retval = 'object type cannot be converted to float'
	return retval 

3, 同时处理多个异常的except语句
def safe_float(obj):
	try:
		retval = float(obj)
	except (ValueError,TypeError):
		retval = 'argumnet must be a number or numeric string'
	return retval 

4, 异常参数
#multiple exceptions 
except (Exception,..,ExceptionN)[,reason]:
	suite_for_Exception1_to_ExceptionN_with_Argment
上面的reason是一个包含异常代码诊断细信息的类实例，异常参数自身会组成一个元组并存储为reason的属性args

5, 获取异常的错误信息
def safe_float(object):
	try:
		retval = float(obeject)
	except (ValueError,TypeError),e:
		retval = str(e)
	return retval 

6, else子句
else子句执行的条件: try范围中的所有代码没有引发异常
try:
	module.function()
except:
	print 'error'
else:
	print 'success'
	
7, finally 子句
finally子句: 无论是否有异常发生，都会执行一段代码

8, try-except-else-finally语句
try:
	A
except MyException:
	B
else:
	C
finally:
	D
结果:A-C-D正常 或 A-B-D异常

9,try语句后跟子句
有else子句则一定有except子句
finally子句前可以没有except或者else子句

10, 上下文管理器
with语句用来简化try-except-finally语句，仅工作于支持上下文管理协议的对象
with open('/etc/passwd','r') as f:
	for eachLine in f:
		# ... do stuff with eachLine or f ...

11, 上下文管理协议
上下文管理器必须实现的方法:
__context__(): 提供上下文对象
__enter__(): 完成with语句块执行前的准备工作
__exit__(): 当with语句块执行结束调用
contextlib模块的functions/decorators,可以方便地创建上下文管理器

12, 触发异常 
通过raise语句，可手动触发异常
语法: raise [SomeException[,args[,traceback]]]
-SomeException: 字符串/异常类/实例
-args: 异常的参数是一个元组
-traceback: 用于exception-normally的追踪对象 
try:
	raise IOError,'raise test'
except IOError,e:
	print e 

13,断言
assert 可用于触发异常: 如果断言成功不采取任何措施,否则触发AssertionError

try:
	assert 1 ==0,'One does not equal zero silly!'
except AssertionError,args:
	print '%s:%s' % (args.__class__.__name__,args)
断言的原理:
def assert(expr,args=None):
	if __debug__ and not expr:
		raise AssertionError,args
	
14,标准异常
所有的标准/内建异常，自定义异常都是继承自根异常 BaseException
#使用异常的目的与好处
目的: 为了使程序足够健壮，可以处理应用级别的错误，并提供用户级别的错误信息
好处: 异常不仅简化代码，而且简化整个错误管理体系

15,异常和sys模块
通过sys模块中exc_info()获取异常信息

import math,cmath
def safe_sqrt(num):
	try:
		result = math.sqrt(num)
	except ValueError:
		result = cmath.sqrt(num)
	return result 

if __name__ == '__main__':
	print safe_sqrt(123)
	print safe_sqrt(-123)






