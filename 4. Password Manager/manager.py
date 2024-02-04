password = input("What is your master password?")

while True:
    mode = input(
        "Would you like to enter a new password or view your previous passwords?(PRESS Q TO QUIT!) ")
    if mode == "Q" or mode == "q":
        break

    if mode == "view":
        pass
    if mode == "add":
        pass
    else:
        print("Your choice is invalid.")
        continue
