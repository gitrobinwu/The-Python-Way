#-*- coding:utf-8 -*- 
def counter(start_at=0):
	count = [start_at]
	def incr():
		count[0] += 1
		return count[0]
	return incr 
count = counter(5)
print count()
print count.func_closure[0].cell_contents 
print count.__closure__[0].cell_contents 
count2 = counter(100)
print count2()
print count() 

