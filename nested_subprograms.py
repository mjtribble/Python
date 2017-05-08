# Nested subprograms

def foo(my_data):
	for d in my_data:
		some_operation(d)
def some_operation(d):
	print d

data = [1,2,3,4,5]
foo(data)

#-----------------------------------------------------

# Helper nested function

def test_func(my_data):
	# define a function w/in a funtion
	def helper_of_test(d):
		print d

	for d in my_data:
		helper_of_test(d)

data = [1,2,3,4]
#variable can be assigned to a function
myfunc = test_func(data)
