from sys import argv

script, num = argv

def fib(n):
	seq = list()
	a,b = 0,1
	while a <= n:
		seq.append(a)
		a,b = b,a+b
	for item in seq:
		print item,
	
	    

fib (int(num))

