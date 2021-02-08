# 2) Write a Python function to create and print a list where the values are
#    square of numbers between 1 and 20 (both included).


def printValues():
	l = list()
	for i in range(1,20):
		l.append(i**2)
	print(l)
	print(tuple(l))
printValues()



