# Counter, nonlocal doesn't work =(

# def make_counter():
#     next_value = 0
#     def return_next_value():
#         nonlocal next_value
#         val = next_value
#         next_value += 1
#         return val
#     return return_next_value

# my_first_counter = make_counter()
# my_second_counter = make_counter()
# print(my_first_counter())
# print(my_second_counter())
# print(my_first_counter())
# print(my_second_counter())
# print(my_first_counter())
# print(my_second_counter())

#--------------------------------------------------

def raise_to(n):
  def my_pow(x):
    return x**n
  return my_pow

base_pow_5 = raise_to(5)
print base_pow_5(3)

#-------------------------------------------------

# def outer():
#   y = 0
#   def inner():
#     nonlocal y
#     y+=1
#     return y
#   return inner


# f = outer()

# f()

# f()

# f()
