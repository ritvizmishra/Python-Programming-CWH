# Using for loop
''' numList = []

for i in range(1,5):
    num = int(input(f"Item #{i}: "))
    numList.append(num)
    
print(max(numList)) '''

# Using conditionals
numList = []
greatestNum = 0
for i in range(1,5):
    num = int(input(f"Item #{i}: "))
    numList.append(num)
    
    if(numList[i] > numList[i-1]):
        greatestNum = numList[i]
        
print(greatestNum)


