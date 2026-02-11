num = int(input("Enter number: "))
match num:
    case 1 | 3 | 5:
        print("Odd number")
    case 2 | 4 | 6:
        print("Even number")
    case _:
        print("Number greater than 6")
