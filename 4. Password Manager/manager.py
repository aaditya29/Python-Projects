from cryptography.fernet import Fernet

password = input("What is your master password?")


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("=>")
            print("User:", user, "| Password:", pwd)


def add():
    name = input('UserName: ')
    password = input('Password: ')
    with open('passwords.txt', 'a') as f:
        f.write(name + "=>" + password + "\n")


while True:
    mode = input(
        "Would you like to enter a new password or view your previous passwords?(PRESS Q TO QUIT!) ")
    if mode == "Q" or mode == "q":
        break

    if mode == "view":
        view()
    if mode == "add":
        add()
    else:
        print("Your choice is invalid.")
        continue
