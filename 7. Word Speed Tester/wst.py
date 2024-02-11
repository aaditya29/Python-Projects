import curses  # curses library in Python provides a terminal-independent way to create text-based user interfaces
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, 'Welcome to typing speed test!\n')
    stdscr.addstr("\nPress any key to BEGIN!")
    stdscr.refresh()
    stdscr.getkey()


# overlaying texts
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)

    # looping through every character user typed to store in list of current_text
    # enumerate will give elements from current_Text as well as index
    for i, char in enumerate(current):
        # writing whatever user typed in green color
        stdscr.addstr(0, i, char, curses.color_pair(1))


def wpm_test(stdscr):  # function to add text for test
    target_text = "Type this line to test your typing skills!"
    current_text = []  # what user has typed
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    stdscr.getkey()

    while True:
        stdscr.clear()
        display_text(stdscr, target_text, current_text)
        stdscr.refresh()
        key = stdscr.getkey()  # user typing

        if ord(key) == 27:  # quit if user presses escape
            break

        # deleting texts if user presses backspace key
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)  # else add texts

        # appending to current text whatever user typed
        current_text.append(key)


def main(stdscr):
    # stylising the texts on screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)
