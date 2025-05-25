listHybrid = ["apple", "cider", "vinegar", 2, 32, 234.23, 'r', 92.4422, False]
listNum = [2,24, 123.12, 34.43, 89]

listNum[4] = 98
print(listNum)
print(listHybrid[3])

# Sorting the List
listNum.sort()
print(listNum)

# Appending to the list
listNum.append(0)
print(listNum)

# Reversing the list
listHybrid.reverse()
print(listHybrid)

# Inserting in the list
listNum.insert(3, 15)
print(listNum)

# Deleting element from the list
listHybrid.pop(0)
print(listHybrid)

# Removing element from the list
listHybrid.remove("cider")
print(listHybrid)