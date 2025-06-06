'''
Generate a random number.
User guesses the num:
a. num > guess -> select a higher number please...
b. num < guess -> select a lower number please...
c. num == guess -> voila! you took x number of guesses to solve the mystery.

I can use an infinite loop.
'''

import random

generatedNum = random.randint(1, 100)
attemptsCount = 0

while True:
    userInput = int(input("\nGuess a number b/w 1 and 100: "))
    attemptsCount += 1
    
    if userInput > generatedNum:
        print(f"Attempt #{attemptsCount}")
        print("Select a lower number please...")
    elif userInput < generatedNum:
        print(f"Attempt #{attemptsCount}")
        print("Select a higher number please...")
    else:
        print(f"\nVoila! The number was {generatedNum} and it took you {attemptsCount} attempts to solve the mystery.")
        break
    
