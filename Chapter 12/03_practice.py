num = int(input("Enter a number: "))

# Way 1
initialList = []
for i in range(0,10):
    initialList.append(i+1)
        
mupltiplicationList = [(i, num*i) for i in initialList]
print(mupltiplicationList)

# Way 2:
multiTable = [(i*num) for i in range(1,11)]
print(multiTable)