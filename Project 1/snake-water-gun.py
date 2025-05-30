'''
Player vs Computer

Snake vs Water -> Snake wins
Snake vs Gun -> Gun wins
Water vs Gun -> Water wins
Snake vs Snake -> Draw
Water vs Water -> Draw
Gun vs Gun -> Draw

first to reach 5 points wins the game.
'''

import random

computerMoveList = ["Snake", "Water", "Gun"]
scorePlayer = 0
scoreComputer = 0

while(scorePlayer < 5 or scoreComputer < 5):
    playerMove = input("\nMake your move: ")
    computerMove = random.choice(computerMoveList)
    
    if playerMove.lower() == "snake" and computerMove.lower() == "water":
        scorePlayer += 1
        print(f"You got this, computer moved {computerMove}: [{scorePlayer} - {scoreComputer}]")
    elif playerMove.lower() == "snake" and computerMove.lower() == "gun":
        scoreComputer += 1
        print(f"Oh noooo, computer moved {computerMove}: [{scorePlayer} - {scoreComputer}]")
    elif playerMove.lower() == "water" and computerMove.lower() == "snake":
        scoreComputer += 1
        print(f"Oh noooo, computer moved {computerMove}: [{scorePlayer} - {scoreComputer}]")
    elif playerMove.lower() == "water" and computerMove.lower() == "gun":
        scorePlayer += 1
        print(f"You got this, computer moved {computerMove}: [{scorePlayer} - {scoreComputer}]")
    elif playerMove.lower() == "gun" and computerMove.lower() == "water":
        scoreComputer += 1
        print(f"Oh noooo, computer moved {computerMove}: [{scorePlayer} - {scoreComputer}]")
    elif playerMove.lower() == "gun" and computerMove.lower() == "snake":
        scorePlayer += 1
        print(f"You got this, computer moved {computerMove}: [{scorePlayer} - {scoreComputer}]")
    else:
        print(f"It\'s a draw, computer moved {computerMove}: [{scorePlayer} - {scoreComputer}]")
        continue
    
    if scorePlayer == 5:
        print(f"\nYayyy! you won. Final score: [{scorePlayer} - {scoreComputer}]")
        break
    if scoreComputer == 5:
        print(f"\nOh no! better luck next time. Final score: [{scorePlayer} - {scoreComputer}]")
        break
        
print("\nThank you for playing!")