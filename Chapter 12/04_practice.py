a = int(input("Enter your num: "))
b = int(input("Enter your divisor: "))

try:
    division = a/b
    print(division)
except TypeError:
    print("Enter valid numbers.")
except ZeroDivisionError:
    print("∞...you're trying to divide by 0.")
else:
    print("Division successful.")
finally:
    print("Program done executing.")