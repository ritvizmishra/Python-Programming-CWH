# Opening a file using 'with', automatically closes without a close()

with open("Files/fileTwo.txt", "r") as file:
    print(file.read())
    