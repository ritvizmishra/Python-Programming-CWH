num = int(input("Enter the size (n ≥ 3): "))

for i in range(0,num):
    if i == 0 or i == num-1:
        print("*" * num, end="")
    else:
        print("*", end="")
        print(" " * (num - 2), end="")
        print("*", end="")
    print()