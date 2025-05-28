#  finding factorial

num  = int(input("Enter the num: "))
factorial = 1

if(num == 0):
    print(f"Factorial = {factorial}")
else:
    for num in range (num,1,-1):
        factorial =  num * (num-1)
        
    print(f"Factorial = {factorial}")