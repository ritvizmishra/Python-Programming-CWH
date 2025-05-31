# Wipiing out content of a file:

with open("Files/fileTwo.txt") as file:
    content = file.read()
    
with open("Files/fileTwo.txt", "w") as wipe:
    wipe.write("")