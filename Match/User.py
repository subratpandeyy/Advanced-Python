user = input("Enter username: ")
password = input("Enter password: ")

match (user, password):
    case ("admin", "123"):
        print("Login Success")
    case _:
        print("Login Denied")