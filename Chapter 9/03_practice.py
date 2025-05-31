# Write multiplication table from 2 to 20 and write them to separate files

# Table generator:
def multiplicationTable(num, file):
    for i in range (1,11):
        term = f"{num} X {i} = {num * int(i)}\n"
        with open (file, "a") as f:
            f.write(term)
            
# Table writer
for i in range (1,20):
    multiplicationTable(i+1,f"table_{i+1}.txt")

