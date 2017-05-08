# Filter Functional Programing

X = range(10)

def my_filter(a):
	return a%2 ==0

def mult2(a):
	return 2*a

#print "\t", map(mult2, filter(my_filter, X)
print "\t", filter(lambda a: a % 2 == 0, X)