num = int(input("Enter a number: "))
match num:
    case 10:
        print("Number is 10")
    case 20:
        print("Number is 20")
    case 30:
        print("Number is 30")
    case _:
        print("Number is not 10, 20, or 30")
