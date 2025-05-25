hindiWords = {
    "namaste" : "hello",
    "kaise ho" : "how are you",
    "suprabhat" : "good morning",
    "subhratri" : "good night",
    "madad" : "help"
}

print(f"We have following Hindi words in our dictionary: {hindiWords.keys()}")

lookUp = input("\nPlease enter the word you need to know the meaning of: ")
print(f"\nThe meaning of {lookUp} is {hindiWords.get(lookUp)}.")