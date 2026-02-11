n = int(input("Enter number: "))
match n:
    case x if x < 0:
        print("Negative number")
    case x if 0 <= x <= 10:
        print("Between 0 and 10")
    case x if 11 <= x <= 20:
        print("Between 11 and 20")
    case _:
        print("Greater than 20")
