# Appending to a file:

str = "\n\nFound absolutely zero motivation from the above poem."

file = open("poem.txt", "a")
file.write(str)
file.close()

