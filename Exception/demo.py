try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = a/b
    print(a)
    print(b)
    print("Result: ",c)

except ZeroDivisionError as z:
    print(z)
