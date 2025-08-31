import hashlib
import getpass

password_manager = {}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def create_account():
    username = input("Enter your desired username: ")
    if username in password_manager:
        print("Username already exists!")
        return
    password = getpass.getpass("Enter your desired password: ")
    password_manager[username] = hash_password(password)
    print("Account has been created")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    if username in password_manager and password_manager[username] == hash_password(password):
        print("Login Successful!")
    else:
        print("Invalid username or password.")

def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()

