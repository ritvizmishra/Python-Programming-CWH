# Make a copy of existing file:

with open("Files/this.txt", "r", encoding="utf-8") as file:
    content = file.read()
    
with open("Files/this_02.txt", "w") as copy:
    copy.write(content)