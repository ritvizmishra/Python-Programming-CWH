# Comparing two files:

with open("Files/this.txt", "r", encoding="utf-8") as first_file:
    first_content = first_file.read()
with open("Files/this_02.txt", "r", encoding="utf-8") as second_file:
    second_content = second_file.read()

if first_content == second_content:
    print("Exactly same.")
else:
    print("Not same.")