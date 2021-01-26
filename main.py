# I’ll walk you through how to make a rock, paper, and scissors game with Python.
# In the rock, paper and scissors game our goal is to create a command-line game
# where a user has the option to choose between rock, paper and scissors and if the user wins the score is added,
# and at the end when the user finishes the game, the score is shown to the user.


# To create the Rock, Paper and Scissors game with Python,
# we need to take the user’s choice and then we need to compare it with the
# computer choice which is taken using the random module in Python from a list of choices, and if the user wins then the score will increase by 1:

import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpuScore = 0
playerScore = 0

while True:
    player = input("Rock, Paper or  Scissors?").capitalize()

    ## Conditions of Rock, Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpuScore += 1
        else:
            print("You win!", player, "smashes", computer)
            playerScore += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpuScore += 1
        else:
            print("You win!", player, "covers", computer)
            playerScore += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpuScore += 1
        else:
            print("You win!", player, "cut", computer)
            playerScore += 1
    elif player == "End":
        print("Final Scores:")
        print(f"CPU:{cpuScore}")
        print(f"Plaer:{playerScore}")
        break
