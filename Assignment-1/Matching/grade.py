grade = input("Enter grade: ").upper()

match grade:
    case "A":
        print("Outstanding")
    case "B":
        print("Excellent")
    case "C":
        print("Good")
    case "D":
        print("Fair")
    case "F":
        print("Fail")    
    case _:
        print("Invalid grade")
