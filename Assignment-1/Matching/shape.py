shape = input("Enter shape: ").lower()

match shape:
    case "circle":
        r = int(input("Radius: "))
        print("Area of circle:", 3.14 * r * r)
    case "square":
        s = int(input("Side: "))
        print("Area of square:", s * s)
    case "rectangle":
        l = int(input("Length: "))
        b = int(input("Breadth: "))
        print("Area of rectangle:", l * b)
    case _:
        print("Unknown shape")
