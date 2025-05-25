sentence = "ritviz mishra ji is a brilliant student."

# String Slice Function
stringSlicer = sentence[3:37]
print(stringSlicer)

# Find the length of the String
stringLength = len(sentence)
print(stringLength)

# Count occurrence of a character
charRepeat = sentence.count('i')
print(charRepeat)

# Remove characters from string
stringRemover = sentence.replace("ji ", "")
print(stringRemover)

# Capitalizing a word in string
stringCapitalize = sentence.capitalize()
print(stringCapitalize)

# Finding characters in string
stringFinder = sentence.find("i")
print(stringFinder)

# Escape sequence character
doubleQuote = "She said: \"Hi, Ritviz.\""
print(doubleQuote)

# No escape seq with \
noEscSeq = r"C:\User\Ritviz"
print(noEscSeq)