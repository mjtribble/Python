def double_my_val(x):
	return 2*x
my_range = range(10)
double_my_range = map(double_my_val, my_range)
print double_my_range
