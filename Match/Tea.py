choice = input('''Enter your choice:\n- Tea\n- Coffee\n- Snacks\n''')
choice.lower()
match choice:
    case "tea":
        print("Your choice is Tea")
    case "coffee":
        print("Your choice is Coffee")
    case "snacks":
        print("Your choice is Snacks")
    case _:
        print("Sorry invalid choice")