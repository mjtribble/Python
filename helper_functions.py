def test_func(my_data):

	def helper_of_test(d):
		print d

	for d in my_data:
		helper_of_test(d)

data = [1,2,3,4]
test_func(data)

