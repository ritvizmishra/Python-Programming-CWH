def factorial(num):
    # base function
    if num == 0 or num == 1:
        return 1
    else:
        # recursive func
        return num * factorial(num-1)
    
num = int(input("Enter the num: "))
print(factorial(num))