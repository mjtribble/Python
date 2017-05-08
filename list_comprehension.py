double_my_range = [2*i for i in range(10)]
print double_my_range

#-----------------------------------------------------
# Using a function
def double_my_val(x):
	return 2*x

my_range = range(10)
double_my_range2 = [double_my_val(my_range)]
print double_my_range2

#-----------------------------------------------------
# prints evens
X = range(10)
print "\t", [ x for x in X if x%2==0]

#-----------------------------------------------------
# doubles each index of range

def mult2(a):
	return 2*a
print [mult2(x) for x in X]

#------------------------------------------------------
# filter function for printing evens

print filter(lambda a: a%2 ==0, X)