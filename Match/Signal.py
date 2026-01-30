signal = input("Enter a signal:\n- Red\n- Yellow or Orange\n- Green or Blue\n")
signal.lower()
match signal:
    case "red":
        print("Stop!!!")
    case "yellow" | "orange":
        print("Get ready...")
    case "green" | "blue":
        print("Go!")
    case _:
        print("Invalid choice")