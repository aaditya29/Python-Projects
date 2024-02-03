import random

highest_range = input("Write a number of your chocie: ")

if highest_range.isdigit():
    highest_range = int(highest_range)

    if highest_range <= 0:
        print("Please enter a positive number!")
        quit()


random_number = random.randint(0, highest_range)
guesses = 0
