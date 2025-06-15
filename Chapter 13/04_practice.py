numbers = [5,55,555,23,52,62,14,65,62,95,90,510,60]
div_by_5 = lambda x : x % 5 == 0

check = list(filter(div_by_5, numbers))
print(check)
