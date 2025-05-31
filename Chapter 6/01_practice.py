# Using for loop
''' numList = []

for i in range(1,5):
    num = int(input(f"Item #{i}: "))
    numList.append(num)
    
print(max(numList)) '''

# Using conditionals
greatestNum = None

for i in range(0,4):
    num = int(input(f"Item #{i+1}: "))
    
    if(greatestNum is None or greatestNum < num):
        greatestNum = num

print(greatestNum)
        


