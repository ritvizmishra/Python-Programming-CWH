# Updating the highscore:

import random

# Game function, returns score as integer:
def game():
    # Generating integer as the score
    userScore = random.randint(1,100)
    print(f"Your score is {userScore}")
    
    # Fetching current high score
    with open("hi-score.txt") as file:
        currentHighScore = file.read()
        if currentHighScore != "":
            currentHighScore = int(currentHighScore)
        else:
            currentHighScore = 0
    
    # Updating the high score
    if currentHighScore < userScore:
        with open("hi-score.txt", "w") as content:
            content.write(f"{userScore}")
    
    return userScore  

game()