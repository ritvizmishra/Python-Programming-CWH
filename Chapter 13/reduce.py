from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9,10]
add = lambda a,b : a + b

add_numbers = reduce(add, numbers)
print(add_numbers)