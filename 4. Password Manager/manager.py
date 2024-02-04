from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


password = input("What is your master password? ")

key = load_key() + password.encode()
fer = Fernet(key)  # initialising encryption module


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("=>")
            print("User:", user, "| Password:", str(
                fer.decrypt(pwd.encode()).decode()))


def add():
    name = input('UserName: ')
    password = input('Password: ')
    with open('passwords.txt', 'a') as f:
        # taking password and encrypting it
        f.write(name + "=>" + str(fer.encrypt(password.encode())) + "\n")


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
