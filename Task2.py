
import random

options = ("rock", "paper", "scissors")
working = True

while working:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Oops It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win bingo!")
    elif player == "paper" and computer == "rock":
        print("You win bingo!")
    elif player == "scissors" and computer == "paper":
        print("You win bingo!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        working = False

print("Thanks for playing!")