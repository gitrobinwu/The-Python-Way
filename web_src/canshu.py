#-*- coding:utf-8 -* 
def tupleVarArgs(arg1,arg2='defaultB',*theRest):
	print 'format arg 1:',arg1
	print 'formal arg 2:',arg2 
	for eachXtrArg in theRest:
		print 'another arg:',eachXtrArg

tupleVarArgs('abc',123,'xyz',456.789)

def newfoo(arg1,arg2,*nkw,**kw):
	'display regular args and all variable args'
	print 'arg1 is:',arg1 
	print 'arg2 is:',arg2 
	for eachNKW in nkw:
		print 'additional non-keyword arg:',eachNKW
	for eachKW in kw.keys():
		print "additional keyword arg '%s':%s" % \
			(eachKW,kw[eachKW])
newfoo('wolf',3,'projects',freud=90,gamble=96)

aTuple = (6,7,8)
aDict = {'z':9}
# 非关键字可变长参数 关键字变量参数 
newfoo(1,2,3,x=4,y=5,*aTuple,**aDict)

