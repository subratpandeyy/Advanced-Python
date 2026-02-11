day = input("Enter day: ").lower()
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Working day")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")
