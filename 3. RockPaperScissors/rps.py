import random

user_wins = 0
computer_wins = 0

game = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter ROCK, PAPER, SCISSORS OR 0 To Quit: ").lower()
    if user_input == "0":
        break

    if user_input not in game:
        continue
