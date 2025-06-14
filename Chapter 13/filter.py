numbers = [1,2,3,4,5,6,7,8,9,10]

def even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = list(filter(even, numbers))
print(even_numbers)