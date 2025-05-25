# Taking users' input to create a list
fruitList = []

for i in range(0, 7):
    fruitName = input(f"Enter the fruit #{i+1} to the list: ")
    fruitList.append(fruitName)
    
print(f"\nList of the fruits you entered: {fruitList}")