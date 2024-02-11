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
    stdscr.addstr(1, 0, f"WPM: {wpm}")
    # looping through every character user typed to store in list of current_text
    # enumerate will give elements from current_Text as well as index
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)  # green if typed correct text
        if char != correct_char:
            color = curses.color_pair(2)  # red if wrong text typed
        # writing whatever user typed in green color
        stdscr.addstr(0, i, char, color)


def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):  # function to add text for test
    target_text = load_text
    current_text = []  # what user has typed
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:  # making sure program doesn't crashes if user types nothing
            key = stdscr.getkey()  # user typing
        except:
            continue

        if ord(key) == 27:  # quit if user presses escape
            break

        # deleting texts if user presses backspace key
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)  # else add texts

        # appending to current text whatever user typed
        current_text.append(key)


def main(stdscr):
    # stylising the texts on screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(
            2, 0, "Your writing speed test is completed. Press any key to continue or ESC to exit!!!")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)
