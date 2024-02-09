import curses  # curses library in Python provides a terminal-independent way to create text-based user interfaces
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome to typing speed test!')
    stdscr.refresh()
    stdscr.getkey()  # waits for user to type on screen


wrapper(main)
