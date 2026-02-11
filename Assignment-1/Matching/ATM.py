balance = 10000
choice = input("1-Check Balance  2-Withdraw  3-Deposit: ")

match choice:
    case "1":
        print("Balance:", balance)
    case "2":
        amt = int(input("Enter amount: "))
        print("Withdrawn:", amt)
    case "3":
        amt = int(input("Enter amount: "))
        print("Deposited:", amt)
    case _:
        print("Invalid option")
