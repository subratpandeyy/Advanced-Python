x = int(input("Enter x: "))
y = int(input("Enter y: "))

match (x, y):
    case (0, 0):
        print("Origin")
    case (_, 0):
        print("X-axis")
    case (0, _):
        print("Y-axis")
    case (a, b) if a > 0 and b > 0:
        print("1st Quadrant")
    case (a, b) if a < 0 and b > 0:
        print("2nd Quadrant")
    case (a, b) if a < 0 and b < 0:
        print("3rd Quadrant")
    case _:
        print("4th Quadrant")
