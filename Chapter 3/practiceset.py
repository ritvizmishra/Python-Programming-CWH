from datetime import date

# Taking input and printing Good morning
name = input("Hey there! What do we call you?\nHello! I am ")
message = f"\nGood morning, \'{name}\'!"
print(message)

str = f"Hey {name}, I hope you're doing  well."

# Detecting double space
detectDoubleSpace = str.find("  ")
# print("Double space at the index number: ",detectDoubleSpace)

# Removing double space
removeDoubleSpace = str.replace("  ", " ")

# Entering Name and Date
confirmation = f'''
{removeDoubleSpace}
Your meeting with us is scheduled for {date.today().strftime("%B %d, %Y")}.
Can\'t wait to see you!
'''
print(confirmation)