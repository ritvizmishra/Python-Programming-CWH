#  Reading a file line by line.

file = open("Files/poem.txt")
line = file.readline()

while(line != ""):
    print(line)
    line = file.readline()
    
file.close()