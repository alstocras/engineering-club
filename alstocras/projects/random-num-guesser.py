import random

numberToBeGuessed = random.randint(-100, 100)
currentGuess = float("inf")
guessCounter = 0
numOfGuesses = 8

while (numberToBeGuessed != currentGuess) & (guessCounter <= numOfGuesses):
    currentGuess = int(input(f"Guess an integer between -100 and 100. You have {8 - guessCounter} guess(es). "))
    if currentGuess > numberToBeGuessed:
        print("you're above the number!")
        guessCounter += 1
    elif currentGuess < numberToBeGuessed:
        print("you're below the number!")
        guessCounter += 1
    elif currentGuess == numberToBeGuessed:
        print("aMaZiNg youve guessed it hehehe")
if guessCounter > numOfGuesses:
    print(f"you've run out of guesses :( The number was {numberToBeGuessed}")
    
    