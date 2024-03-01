from cryptography.fernet import Fernet

psswrd = input("Input master password: ")

def rightKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


rightKey()


def peek():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, ", Password:", passw)

def add():
    user = input("Input Username: ")
    pwd = input("Input Password: ")

    with open("passwords.txt", "a") as f:
        f.write(user + "|" + pwd + "\n")
    
while True:
    mode = input("Add new password or view existing passwords (view, add)? Enter Q to quit. ").lower()
    if mode == "q":
        break

    if mode == "view":
        peek()
    elif mode == "add":
        add()
    else:
        print("Error: Invalid Request")
        continue