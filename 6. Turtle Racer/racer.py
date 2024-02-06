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


def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            # moving between 1 to 20 pixel range
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:  # checking if passed the finish line
                # returning color of winner turtle
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
        return turtles


def initialize_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racer')


racers = racer_numbers()
initialize_screen()

random.shuffle(COLORS)
# selecting number of racers
colors = COLORS[:racers]

winner = race(colors)
print("The winner is ", winner, "turtle.")
time.sleep(10)
