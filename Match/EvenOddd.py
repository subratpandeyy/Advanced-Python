num = int(input("Even or Odd: "))
match num:
    case num if num%2==0:
        print("Even")
    case _:
        print("Odd")