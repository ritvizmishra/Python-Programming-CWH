from functools import reduce

numbers = [23,42,52,12,52,8,3,63,47,25,66]

max_val = reduce(lambda a,b : a if a>b else b, numbers)
print(max_val)