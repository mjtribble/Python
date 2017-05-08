X = [1,2,3,4,5]
count = 0
for i in X:
	count +=1
print count

#---------------------------------------------------------
# Reduce takes function and applies to every element of set y
# reduces the iterable to a single value and returns

def my_updater(agg, item):
	return agg + 1
y = [2, 4, 6]
print reduce(my_updater, y)

#-----------------------------------------------------
# This does the same thing as the reduce
count = 0
for i in X:
	count = my_updater(count, i)
print count

def my_max(agg, item):
	return agg if agg > item else item

def reduce(my_op, my_set, my_init_value):
	v = my_init_value
	for i in my_set:
		v = my_op(v, i)



