#-*- coding:utf-8 -*- 
--->掌握基础语法--->高级特性-->web框架flask/mongodb-->开发个人博客
-->网络爬虫包--->数据库mongodb/redis/mysql-->数据分析

主题: python常见数据结构整理
# pyhton 中常见的数据结构可以统称为容器(container)
# 序列(如列表和元组)，映射(如字典)以及集合(set)三大类

#1, 序列(列表，元组和字符串)
# 序列中每个元素都有自己的编号。Python有6种内建的序列。其中列表和元组是最常见的类型。
#其他包括字符串，Unicode字符串，buffer对象和xrange对象。

#1,列表
#列表是可变的，这是区别于字符串和元组的最重要的特点，一句话概括： 列表可以修改，而字符串和元组不能

list1 = ['hello','world']
print list1 
list2 = [1,2,3]
print list2 

#函数方式创建 
list3 = list("hello")
print list3 

2,元组
元组和列表是一样，也是一种序列，唯一不同的是元组不能被修改

只有一个值的元组，必须加个逗号(,);
tuple()函数
tuple函数和序列的list函数一样：以一个序列作为参数转换成元组

3, 字符串
 字符串格式化使用字符串格式化操作符%实现
str1 = 'Helllo,%s' % 'world'
print str1 


格式化操作符的右操作数可以是任何东西，如果是元组或者映射类型(字典)
strs = ('Hello','world')
str1 = '%s,%s' % strs 
print str1 
d = {'h':'Hello','w':'World'}
str1 = '%(h)s,%(w)s' % d
print str1 

#如果需要输出%这个特殊字符，会转义
str1 = "%s%%" % 100
print str1 

#对数字进行格式化处理，通常需要控制输出的宽度和精度:
from math import pi 
str1 = '%.2f' % pi #精度2
str1 = '%10%' % pi 字段宽10 
print str1 
str1 = '%10.2f' % pi #字段宽10，精度2

# python中string模块提供了另外一种格式化值的方法:模板字符串
from string import Template 
str1 = Template('$x,$y!')
str1 = str1.substitute(x='Hello',y='world')
print str1 

# 如果替换字段是单词的一部分，那么参数名称就必须用括号括起来，从而精确指明
from string import Template 
str1 = Template('Hello,w${x}d!')
str1 = str1.substitute(x='orl')
print str1 

#如果输出符，可以使用$输出
from string import Template 
str1 = Template('$x$$')
str1 = str1.substitute(x='100')
print str1 

#除了关键字之外，模板字符串还可以使用字典变量提供键值对进行格式化
from string import Template 
d = {'h':'Hello','w':'world'}
str1 = Template('$h,$w')
#关键字或者字典替换
str1 = str1.substitute(d)
print str1 

4, 通用序列操作(方法)
#从列表，元组以及字符串可以"抽象"出序列的一些公共通用方法
#这些操作包括: 索引，分片，加，乘以及检查某个元素是否属于序列的成员
#计算序列长度，最大最小元素等内置函数

(1),索引
str = 'hello'
nums = [1,2,3,4]
t1 = (123,234,345)
print str1[0],str[-1]
print nums[1],nums[-2]
print t1[2],t1[-3]

(2),分片
#分片操作用来访问一定范围内的元素。分片通过冒号相隔的两个索引实现
nums = range(10)
print nums 
print nums[1:5],nums[-3:-1],nums[-3:],print nums[:]

#不同步长有不同的输出
print nums[0:10],nums[0:10:2]

(3),序列相加
str1 = 'Hello'
str2 = 'world'
print str1 + str2 
num1 = [1,2,3]
num2 = [2,3,4]
print num1+num2 

(4)乘法
print [None]*10
str1 = 'Hello'
print str1*2
num1 = [1,2]
print num1*2

(5)成员资格
#in运算符会用来检查一个对象是否为某个序列的成员
str = 'Hello'
print 'h' in str1
print 'H' in str1
num1 = [1,2]
print 1 in num1

(6)长度，最大最小值
#通过内建函数len,max和min可以返回序列中所包含元素的数量，最大和最小元素
str1 = 'Hello'
print len(str1)
print max(str1)
print min(str1)

num1 = [1,2,1,3,123]
print len(num1),max(num1),min(num1)


二，映射(字典)
字典(也叫散列表)是Python唯一内建的映射类型

1, 键类型
字典的键可以是数字，字符串或者元组，键必须唯一。
Python中，数字，字符串和元组都设计成不可变类型
而最常见的列表以及集合都是可变的，所以列表和集合不能作为字典的键
键为任何不可变类型，这正是python中字典最强大的地方。

2, 自动添加
即使键在字典中并不存在，也可以为它分配一个值，这样字典就会建立新的项

3, 成员资格
item in d查找的是键，而不是值

三，集合
strs = set(['jeff','wong','cnblogs'])
nums = set(range(10))

add 和remove 
set1 = set([1])
print set1 
set1.add(2)
print set1 
set1.remove(2)
print set1 










