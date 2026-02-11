lst = [1, 2, 3]
match len(lst):
    case 0:
        print("Empty list")
    case 1:
        print("List has one element")
    case 2:
        print("List has two elements")
    case _:
        print("List has many elements")
