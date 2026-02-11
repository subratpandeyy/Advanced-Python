a=int(input("Enter the first side of the triangle: "))
b=int(input("Enter the second side of the triangle: "))
c=int(input("Enter the third side of the triangle: "))
sum=a+b+c
if a>0 | b>0 | c>0 and sum==180:
    print("The triangle is valid")
else:
    print("The triangle is not valid")    