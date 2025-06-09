'''
List comprehension is a shorter and cleaner way to create a list from an existing iterable (like a list, range, etc.) — all in one line.

--> Syntax:
[expression for item in iterable if condition]
'''
numbers = [0,1,2,3,4,5,6,7,8,9,10]
sq_numbers = [(item, item ** 2) for item in numbers]
print(sq_numbers)

cube_numbers = [(n, n**3) for n in range(11)]
print(f"{cube_numbers}")