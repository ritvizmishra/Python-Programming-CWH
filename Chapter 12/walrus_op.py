# Example 1
if (n := len([1,2,3,4,5,6,7,8,9,0])) > 5:
    print(f"List too long, expected <= 5, actual {n}")

#Example 2
while(line := input("Continue or enter 'quit': ")) != 'quit':
    print(f"You entered: {line}") 
