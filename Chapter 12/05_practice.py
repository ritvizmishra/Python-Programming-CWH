num = int(input("Enter a number: "))

multiTable = [(i*num) for i in range(1,11)]
print(multiTable)

with open("Chapter 12//Files//Table.txt", "a") as file:
    file.write(f"\n{num}: {multiTable}")