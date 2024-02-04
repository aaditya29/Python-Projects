password = input("What is your master password?")


def view():
    pass


def add():
    pass


while True:
    mode = input(
        "Would you like to enter a new password or view your previous passwords?(PRESS Q TO QUIT!) ")
    if mode == "Q" or mode == "q":
        break

    if mode == "view":
        view
    if mode == "add":
        add
    else:
        print("Your choice is invalid.")
        continue
