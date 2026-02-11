a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
if a>=b and a>=c:
    print("the largest number is a")
elif b>=a and b>=c:
    print("The largest number is b")
else:
    print("The largest number is c")        