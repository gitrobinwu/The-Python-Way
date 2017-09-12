#-*- coding:utf-8 -*- 
主题: 文件和输入输出

# 文件对象(内建函数，内建方法，属性) ,标准文件，访问系统的方法，文件执行，初步认识持久化存储和标准库猴子那个与文件相关的模块

1，文件内建函数
#1, open() 
file_object = open(file_name,access_mode='r',buffering=-1)

#2, file() 
建议使用open()来读写文件，而在处理文件对象时使用file() if instance(f,file)

2, 文件内建方法
#1. 输入
file.xreadlines() 不是一次性读取所有的行，而是每次读取一块，所以用在for循环时可以减少对内存的占用，和使用iter(file), for eachline in file是一样的


#2, 输出
输出方法read() 或者readlines()从文件中读取行时，Python并不会删除结束符;
输出方法write()或者writelines() 不会自动加入行结束符，需要在向文件写数据前自动加入行结束符

#3, 文件内移动
seek(offset=0):在文件中移动文件指针到不同的位置，offset字节代表相对于某个位置的偏移量
tell() :返回当前位置的偏移量
truncate(size=file.tell()): 截取文件到最大size字节，默认为当前文件位置

3, os模块内建方法
os.linesep(): 行分隔符
os.sep() 路径名分隔符

4, 文件内建属性
f.closed f.mode f.encoding f.name 

5, commandline参数
argc和argv分别代表参数个数和参数向量
sys.argv[0]程序名称
处理命令行参数的模块:getopt模块 oprparse模块

6, os模块
read()/write() 根据文件描述符读取/写入数据
remove()、unlink() 删除文件
mkidr() makedirs() 创建目录,创建多层目录
rmdir,removedirs() 删除目录，删除多层目录

7, os.path 模块
basename() 去掉目录路径，返回文件名
dirname() 去掉文件名，返回目录路径
exists() 指定路径(文件或目录)是否存在 
isabs() 指定路径是否为绝对路径
isdir() 指定路径是否存在且为一个目录
isfile() 指定路径是否存在一个文件
islink() 指定路径是否存在为一个符号链接


	










