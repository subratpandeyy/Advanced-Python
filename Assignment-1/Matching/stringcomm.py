cmd = input("Enter command: ").lower()
match cmd:
    case "start":
        print("System started")
    case "stop":
        print("System stopped")
    case "exit":
        print("Exiting program")
    case _:
        print("Invalid command")
