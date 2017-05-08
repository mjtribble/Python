def curry (f, x):
	return lambda y: f(x, y)

#General curry function
def general_curry(f, x):
	return lambda *args, **kwargs: f(x, *args, **kwargs)

def times123(x, xx, yy, y=1, z=2):
	return x * y * z * xx * yy

def mult(x, y):
	return x * y

mult4 = curry(mult, 4)
print mult4(6)

print times123( 1, 2, 3, y = 4, z = 5)

times23 = general_curry(times123, 1)
print times23(2, 3, y=4, z=5)