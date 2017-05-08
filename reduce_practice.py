from random import shuffle
from functools import reduce

def question1():
	my_range = range(97, 123)
 	print [chr(i) for i in my_range]

def question2():
	def raise_to(n):
  		def my_pow(x):
    			return x**n
  		return my_pow

	base_pow_5 = raise_to(5)
	print base_pow_5(3)


	my_range = range(10)
	for x in my_range:
		alphabet = [(x,y)for y in my_range]
		print alphabet

def question3():
	my_range = range(10)
	print [(x, y) for x in my_range for y in my_range]

def question4():
	my_range = range(1,11)
	def convert_number_to_letter(n):
	 	return chr(n+96)

	list = [(convert_number_to_letter(letter), number) for letter in my_range for number in my_range]
	#shuffle(list)
	print list

def question5():
	my_input = raw_input("What do you want to search for?: ")
	def my_updater(count, item):
		if item[0] == my_input:
			count += 1
		return count

	print reduce(my_updater, [('a',1), ('b',3), ('a',2)], 0)



def question6():
	my_input = raw_input("What do you want to search for?: ")

	def my_updater(add, item):
		if item[0] == my_input:
			add += item[1]
		return add

	print reduce(my_updater, [('a',10), ('b',3), ('a',2)], 0)


def question7():
	my_input = raw_input("What do you want to search for?: ")
	count = 0
	def my_updater(average, item):
		global count
		if item[0] == my_input:
			if count == 0:
				average += item[1]
			else:
				average += item[1]/2
			count + 1
		return average
	my_list = [('a',10), ('b',3), ('a',2)]
	print reduce(my_updater, my_list, 0)


def main():
	#question1()
	question2()
	#question3()
	#question4()
	#question5()
	#question6()
	#question7() #more to do...


if __name__ == '__main__':
    main()


