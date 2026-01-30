day = input("Enter a week day: ")
day.lower()
match day:
    case "sunday":
        print("Sunday - Weekend")
    case "monday":
        print("Monday - Weekday")
    case "tuesday":
        print("Tuesday - Weekday")
    case "wednesday":
        print("Wednesday - Weekday")
    case "thursday":
        print("Thursday - Weekday")
    case "friday":
        print("Friday - Weekday")
    case "saturday":
        print("Saturday - Weekend")
    case _:
        print("Invalid Choice")