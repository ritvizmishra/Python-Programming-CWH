def sumNaturalNum (num):
    if num == 1:
        return 1
    num = num + sumNaturalNum(num-1)
    return num

promptCal = int(input("Enter the num: "))
print(f"Sum of {promptCal} numbers is {sumNaturalNum(promptCal)}")