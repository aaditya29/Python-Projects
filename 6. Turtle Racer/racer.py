import tkinter as tk
import turtle

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'yellow', 'blue', 'green', 'black',
          'purple', 'orange', 'pink', 'brown', 'golden']

screen = turtle.screen
screen.set_width(WIDTH, HEIGHT)
screen.title('Turtle Racer')


def racer_numbers():
    racers = 0
    while True:
        racers = input('Type the number of racers between 2 TO 10: ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not a number. Please Try Again!!')
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10. Try Again!')


racers = racer_numbers()
print(racers)
