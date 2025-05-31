list = ["Shubhan", "Thubhan", "Jhubhan", "Chubhan", "an"]

def removeList(list, word):
    newList = []
    for item in list:
        if not(item == word):
            newList.append(item.strip(word))
    return newList

print(removeList(list, "an"))