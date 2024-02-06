import tkinter as tk
import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'yellow', 'blue', 'green', 'black',
          'purple', 'orange', 'pink', 'brown', 'golden']


def racer_numbers():
    racers = 0
    while True:
        racers = input('Type the number of racers between 2 TO 10: ')
        if racers:
            racers = int(racers)
        else:
            print('Input is not a number. Please Try Again!!')
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range 2-10. Try Again!')


def initialize_screen():
    screen = turtle.screen()
    screen.set_width(WIDTH, HEIGHT)
    screen.title('Turtle Racer')


racers = racer_numbers()
initialize_screen()

racer = turtle.Turtle()  # creating object to move around for turtle
racer.speed(2)
racer.shape('turtle')
racer.forward(100)  # move forward 100 pixels
racer.left(90)
racer.forward(100)  # move forward 100 pixels
racer.left(90)
racer.backward(100)  # move backward 100 pixels
time.sleep(5)
