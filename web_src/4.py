#-*- coding:utf-8 -*-
主题: 函数创建，调用方式，内部函数，函数装饰器，函数参数的定义和传递，函数式编程，变量作用域，闭包

1, 函数
函数是对程序逻辑进行结构化或过程的一种编程方法，实现代码的复用
python的过程就是函数，因为解释器会隐式的返回默认值None
Python动态地确定函数返回类型，而不是进行直接的类型关联
可以使用type()函数作为代理，处理有不同参数类型的函数的多重声明，以模拟其他编程语言的函数重载

2，关键字参数
解释器通过给出的关键字来匹配参数的值

3，参数组
func(*func_grp_nonkw_args,**dict_grp_kw_args):tuple_grp_nonkw_args
以元组形式体现的非keyword参数组，dict_grp_kw_args是装keyword参数的字典

4, 函数属性
def bar():
	pass 
bar.__doc__ == 'OOP,forgot the doc str above'
bar.version = 0.1 

print bar.__doc__
print bar.version 

5, 内部/内嵌函数
内部函数: Pytho支持静态地嵌套域，可以在函数体内创建另一个函数
创建方式: 
  def foo():
	  def bar():
		  print 'bar() called'
	  print 'foo() called'
	  bar(): 

6,函数装饰器
装饰器是在函数调用之上的修饰，当且仅当声明一个函数的时候，才会被额外调用
# AOP 面向切面编程
@deco1(deco_arg)
@deco2
def func(): pass 

=> func = deco1(deco_arg)(deco2(func))

用途:
#1, 引入日志
#2，增加计时逻辑来检测性能
#3，给函数加入事物的能力

7, 形式参数
(1), 位置参数
位置参数必须以被调用函数中定义的准确顺序来传递

(2),默认参数
所有的位置参数必须出现在任何一个默认参数之前
def taxMax(cost,rate=0.0825)
	return cost+(cost*rate)

taxMax(100)
(3),可变长度的参数
在函数调用中使用*和**符号，允许函数接收在函数声明中定义的形参之外的参数

8,非关键字可变长参数(元组)
def tupleVarArgs(arg1,arg2='defaultB',*theRest):
	print 'format arg 1:',arg1 
	print 'format arg 2:',arg2 
	for eachXtrArg in theRest:
		print 'another arg:',eachXtrArg
		
tupleVarArgs('abc',123,'xyz',456.789)

9, 关键字变量参数(Dictionary)
关键字变量参数为函数定义后的最后一个参数
def function_name([formal_args[,*vargst[,**vargsd]])
def newfoo(arg1,arg2,**nkw,**kw):
	'display regular args and all variable args'
	 print 'arg1 is:',arg1 
	 print 'arg2 is:',arg2 
	 for eachNKW in nkw:
		print 'additional non-keyword arg:',eachNKW
	 for eachKW in kw.keys():
		 print "addition keyword arg '%s':%s" % (eachKW,kw[eachKW])
newfoo('wolf',3,'projects',freud=90,gamble=96)

# 调用带有可变长参数对象函数
aTuple = (6,7,8)
aDict = {'z':9}
#非关键字可变长参数 以及 关键字变量参数 
newfoo(1,2,3,x=4,y=5,*aTuple,**aDict)

10,函数式编程
(1), 匿名函数与lambda 
#1, 用lambda关键字创造匿名函数
#2,lambda 表达式的目的在于优化性能，在调用时绕过函数栈的分配
a = lambda x,y=2:x+y 

(2),内建函数apply 
#1， filter(bool_func,seq): bool_func为序列seq的每个元素调用给定布尔函数，将每次filter返回的非零(true)值元素添加到返回列表中
def odd(n):
	return n%2
filter(odd,allNums)
= filter(lambda n:n%2,allNums)	
= [n for n in allNums if n%2]
	
(3),map() 
#map()将函数调用"映射"到每个序列的元素上，并返回一个含有所有返回值的列表
#1, map() 与单个序列	
map((lambda x:x+2),[0,1,2,3,4,5,])
map(lambda x:x**2,range(6))
[x**2 for x in range(6)]	

#2, map()与多个序列
map(lambda x,y:x+y,[1,3,5],[2,4,6]) # --> [3,7,11]
map(lambda x,y:(x+y,x-y),[1,3,5],[2,4,6])
map(None,[1,3,5],[2,4,6])
zip([1,3,5],[2,4,6])

(4), reduce() 
# reduce() 通过取出序列的头两个元素，将他们传入二元函数来获得一个单一的值来实现
reduce(func,[1,2,3]) <=> func(func(1,2),3)
reduce(lambda x,y:x+y,range(1,101))

11,偏函数应用
PFA是在python2.5的时候被引入的，通过functools模块能很好的给用户调用
from operator import add,mul 
from functools import partial
add1 = partial(add,1) # add1(x) == add(1,x)
mul100 = partial(mul,100) # mul100(x) == mul(100,x)

# 将二进制字符串转换成整数: baseTwo(x) == int(x,base=2)
baseTwo = partial(int,base=2)
baseTwo.__doc__ = 'Convert base 2 string to an int.'
baseTwo('10010')

12, 变量作用域
# 当搜索一个变量名的时候，python解释器先从局部作用域开始搜索;
# 如果局部作用域内没有找到变量名，就会在全局域搜索这个变量名;
# 如果在全局域也找不到则抛出NameError异常;
 
13, global语句 
# global 将局部变量变为全局变量
is_this_global = 'xyz'
def foo():
	global is_this_global 
	this_is_local = 'abc'
	is_this_global = 'def'
	print this_is_local+is_this_global 
foo() # abcdef 
print is_this_global # def 

14, 闭包
# 如果在一个内部函数里，对在外部作用域(但不是在全局作用域)的变量存在进行引用，那么内部函数就被认为是closure
# 定义在外部函数内的但由内部函数引用或者使用的变量称为自由变量，使用函数的func_closure属性来追踪自由变量
# 或者使用__closure__属性访问cell对象，访问cell对象中自由变量的内容，使用cell对象属性cell_context 

# closurs多用于GUI或者在很多API支持回调函数的事件驱动编程中。回调和闭包都是函数，但可携带一些其他作用域
def conter(start_at=0):
	count = [start_at]
	def incr():
		count[0] +=1
		return count[0]
	return incr
count = conter(5)
print count() #6 	
#func_closure或者__closure__追踪自由变量 	
#对自由变量的引用存储在cell对象里(cell是在作用域结束后使自由变量存活的一种基础方法)	
print count.func_closure[0].cell_contents #[6]
print count.__closure__[0].cell_contents #[6]

15, 作用域和lambda 
x = 10
def foo():
	y = 5
	bar = lambda z:x+z
	print bar(y) # 15 
	y = 8
	print bar(y) # 18 
foo() 

16, 递归
def factorial(n):
	if n ==0 or n == 1: 
		return 1
	else:
		return (n*factorial(n-1))

17, 生成器
# 挂起返回出中间值并多次继续协同程序被称为生成器
# 当等待一个生成器的时候，生成器能立刻返回控制
# 在调用的生成器能挂起(返回一个结果)之前，调用生成器返回一个结果而不是阻塞等待那个结果的返回
# 那就是yield语句返回一个值给调用者并暂停执行.当生成器的next()方法被调用的时候，它会准确地从离开的地方继续. 
from random import randint 
def randGen(aList):
	while len(aList) > 0:
		yield alist.pop(randint(0,len(aList)))
for item in ranGen(['rock','paper','scissors'])
	print item 

18, 加强的生成器特性
#除了next()来获得下个生成的值，还可以将值回送send()给生成器，以及要求生成器退出close() 
def counter(start_al=0):
	count = start_at 
	while True:
		val = (yield count)
		if val is not None:
			count = val 
		else:
		 count+=1
count = counter(5)
print count.next()
print count.next()
count.send(9)
print count.next() 
count.close() 

19,练习
(1), 实现max()和min()内建函数 
def max2(num1,num2):
	return num1 if num1>num2 else num2

def my_max(seq):
	return reduce(max2,seq)

print my_max([1,5,2,7,3])

lines = filter(lambda line:line.strip()+'\n',open('test.txt'))



	









