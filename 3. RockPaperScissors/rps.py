import random

user_wins = 0
computer_wins = 0

game = ["rock", "paper", "scissors"]

while True:
    user_choice = input(
        "Enter ROCK OR PAPER OR SCISSORS OR Q To Quit: ").lower()
    if user_choice == "Q":
        break

    if user_choice not in game:
        continue

    option = random.randint(0, 2)

    # rock:0, paper:1, scissors:2
    computer_choice = game[option]
    print("Computer picked ", computer_choice + ".")

    if user_choice == "rock" and computer_choice == "scissors":
        print("YOU WON!")
        user_wins += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("YOU WON!")
        user_wins += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("YOU WON!")
        user_wins += 1

    elif user_choice == "scissors" and computer_choice == "paper":
        print("YOU WON!")
        user_wins += 1

    else:
        print("YOU LOST!")
        computer_wins += 1

print("User won ", user_wins, "times.")
print("Computer won ", computer_wins, "times.")
print("GAME OVER!!")
