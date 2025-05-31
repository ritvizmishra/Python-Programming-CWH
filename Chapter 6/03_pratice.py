message = input("Enter your text: ")

spam = [
    "Make a lot of money",
    "buy now",
    "subscribe this",
    "click this"
]

message_lower = message.lower()
isSpam = False

for phrase in spam:
    if(phrase.lower() == message_lower):
        isSpam = True
        break
        
if isSpam:
    print("This is a spam.")
else:
    print("This is not a spam.")