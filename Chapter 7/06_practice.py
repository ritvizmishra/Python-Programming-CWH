#  Finding factorial of a number:

num  = int(input("Enter the num: "))

if num == 0 or num == 1:
    print(f"Factorial of {num} = 1")
else:
    for i in range (num-1,1,-1):
        num *= i
        
    print(f"Factorial of given number = {num}")