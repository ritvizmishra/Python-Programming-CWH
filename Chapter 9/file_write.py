# Writind in an existing file -- this overrides existing data

str = "This is a Gemini generated poem."

file = open("Files/poem.txt", "w")
file.write(str)
file.close()

# Writing in a new file
strTwo = "Creating and wrting in a new file."

file = open("Files/fileTwo.txt", "w")
file.write(strTwo)
file.close()

