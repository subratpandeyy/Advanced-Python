data = {"name": "bulbul", "age": 20}
match data:
    case {"name": n, "age": a}:
        print("Name:", n)
        print("Age:", a)
    case {"name": n}:
        print("Name:", n)
    case _:
        print("No matching keys")
