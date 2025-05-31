# Printing pyramid

num = int(input("Enter the num: "))

for i in range(0,num):
    print(" " * (num - i - 1), end="")
    print("*" * ((i*2) + 1), end="")
    print()