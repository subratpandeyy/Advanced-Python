a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice = input("Enter operator (+, -, *, /): ")
match choice:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        print("Result:", a / b)
    case _:
        print("Invalid operator")
