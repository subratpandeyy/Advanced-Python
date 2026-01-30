num = int(input("Positive or Negative: "))
match num:
    case 0:
        print("ZERO")
    case num if num > 0:
        print("Positive Number")
    case _:
        print("Negative Number")