import random

choices = ["rock", "paper", "scissors"]
print("Yo, let's play!")
print("rock, paper, scissors")

user = input("Your choice: ").lower()

if user not in choices:
    print("Wrong input, game over.")
else:
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if user == computer:
        print("Draw, friendship won!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose, try again!")
