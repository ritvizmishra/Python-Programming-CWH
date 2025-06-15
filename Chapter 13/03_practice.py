num = int(input("Enter num: "))
table = []

for i in range (1,11):
    table.append(str(num*i))   
print(table)

s = "\n".join(table)
print(s)