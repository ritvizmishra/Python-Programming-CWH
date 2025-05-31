# Find out whether file has a certain word:

with open("Files/twinkle.txt") as poem:
    text = poem.read().lower()
    if "twinkle" in text:
        print("yes it contains twinkle")
    else:
        print("no it does not contain twinkle.") 