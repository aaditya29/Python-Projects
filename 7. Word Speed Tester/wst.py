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


def wpm_test(stdscr):  # function to add text for test
    target_text = "Type this line to test your typing skills!"
    current_text = []  # what user has typed
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    stdscr.getkey()


def main(stdscr):
    # stylising the texts on screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)
