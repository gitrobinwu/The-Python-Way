#-*- coding:utf-8 -*- 
主题: 模块和包

python模块以如何把数据从模块中导入到编程环境中。模块是用来组织python代码的方法
而包是用来组织模块的

1, 模块
自我包含并且有组织的代码片段就是模块，模块是按照逻辑来组织Python代码的

2, 模块和文件
文件在物理层上组织模块的方法
一个文件被看作是一个独立模块，一个模块也可以被看作是一个文件

3, 搜索路径和路径搜索
路径搜索:查找某个文件的操作
搜索路径：去查找一组目录
sys.path: 查看当前的搜索路径
sys.modules: 当前导入了哪些模块和来自于什么地方

4,命名空间
命名空间是标识符到对象的映射

Python解释器加载命名空间的顺序:
(1), 先加载内建命名空间__builtins__
(2), 随后加载执行模块的全局命名空间，它在模块开始执行后变为活动的命名空间

5, 变量查找顺序
局部命名空间-->全局命名空间-->内建命名空间

6, 无限制的命名空间
随时都可以给函数添加任何属性

7，多行导入
提倡使用from Tkinter import * 

扩展的import语句（as）
import Tkinter as tk
from cgi import FieldStorage as from 

8, 模块导入的特性
#1, 加载模块会导致这个模块被"执行",也就是被导入模块的顶层代码(包括设定全局变量以及类和函数的声明)将直接执行
#2, 尽可能把代码封装到函数中，只把函数和模块定义放入模块的顶层

9, 导入(import)和加载(load)
#1, 一个模块只被加载一次无论它被导入多少次(防止多重导入时代码被多次执行)
#2，加载只在第一次导入模块时发生

from module import *使用场合
目标模块中的属性非常多，反复键入模块名很不方便
在交互解释器下，为了减少输入模块名的次数

被导入到导入者作用域的名字
只从模块导入名字的副作用是那些名字会成为局部作用域的一部分

10, 关于__future__ 
体验Python新特性: from __future__ import new_fature 

11, 从ZIP文件中导入模块
如果搜索路径中存在一个包含Python模块(.py,.pyc,.pyo)的zip文件，导入时会把ZIP文件当作目录处理，在文件中搜索模块

如果要导入的ZIP文件只包含.py文件，那么Python不会为其添加对应的.pyc文件

12, 模块内建函数
(1), __import__ 
#__import__(module_name[,globals[,locals[,fromlist])
sys = __import__(sys)

(2),gobals()和locals()
内建函数globals()和locals()以字典形式返回调用者的全局命名空间和局部命名空间
在全局命名空间下，globals()和locals()返回相同的字典，因此此时的局部命名空间就是全局空间

(3),reload() 
reload()内建函数： 重新导入一个已经导入过的模块
reload()使用要求： 
 #1， 模块必须是全部导入(不是使用from-import)，而且它已被成功导入
 #2， 参数是模块自身而不是模块名字符串

import sys 
reload(sys) 


二， 包
包是一个有层次的文件目录结构，定义了一个由模块和子包组成的Python应用程序执行环境
模块下的__init__.py文件，用于初始化模块

1, 包的导入
[test.py package main.py]
-- package [__init__.py a.py]
cat test.py
#print 'this is a test'

cat package/__init__.py 
#import test.py 
#db = "this is db"

cat package/a.py
from . import db
print db 

2, from-import all 
包支持from-import all语句: from package.module import * 
[__init__.py中__all__变量包含执行改语句时应该导入的模块名字字符串列表]

3,绝对导入
所有的导入都被认为是绝对的，即这些被导入的模块必须通过Python路径
sys.path或者PYTHONPATH来访问

4,相对导入
from Phone.Mobile.Analog import dial #绝对导入
from .Analog import dial #相对导入
from ..Fax import G3.dial #相对导入

5, 模块的其他特性
sys.modules变量包含当前载入到解释器的模块组成字典key模块名 value 路径

6，阻止属性导入
如果不想让某个模块属性被from module import * 导入，可以在不想被导入的属性名称加上一个下划线,变成私有

7,不区分大小的导入
指定PYTHONCASEOK环境变量，以不区分大小写地导入模块

8,源代码编码
Python默认的编码格式是ASCII，在模块头部指定编码格式
#-*- coding:utf-8 -*- 

9, 模块执行的方式
(1), 通过命令行或shell: python hello.py
(2),通过内建函数execfile():execfile('C:/hello.py')
(3),通过模块导入：import hello
(4),通过解释器的-m选项: python -m SimpleHTTPServer 







