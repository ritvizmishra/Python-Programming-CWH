numbers = [1,2,3,4,5,6,7,8,9,10]

square = lambda x:x*x

squared_numbers = list(map(square, numbers))
print(squared_numbers)