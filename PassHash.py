psswrd = input("Input master password: ")

def peek():
    pass

def add():
    user = input("Input Username: ")
    pwd = input("Input Password: ")

    with open("passwords.txt", "a") as f:
        f.write(user + "|" + pwd)
    
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