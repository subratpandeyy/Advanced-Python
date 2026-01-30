choice = input("Enter an operation:\n+\n-\n*\n/\n%\n")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

match choice:
    case '+':
        print("Sum: ",(num1+num2))
    case '-':
        print("Difference: ",(num1-num2))
    case '*':
        print("Product: ",(num1*num2))
    case '/':
        print("Division: ",(num1/num2))
    case '%':
        print("Modulus: ",(num1%num2))
    case _:
        print("Invalid")