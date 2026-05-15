import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        username = input("Enter username: ")
        password = input("Enter password: ")

        hashed_password = hash_password(password)

        users[username] = hashed_password

        print("User registered successfully.")

    elif choice == "2":

        username = input("Enter username: ")
        password = input("Enter password: ")

        hashed_password = hash_password(password)

        if username in users and users[username] == hashed_password:
            print("Login successful.")
        else:
            print("Invalid username or password.")

    elif choice == "3":
        break

    else:
        print("Invalid option.")