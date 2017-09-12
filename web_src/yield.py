#-*- coding:utf-8 -*- 
from random import randint 
def randGen(aList):
	while len(aList) > 0:
		yield aList.pop(randint(0, len(aList)))

if __name__ == '__main__':
	for item in randGen(['rock','paper','scissors',"sda"]):
		print item 

