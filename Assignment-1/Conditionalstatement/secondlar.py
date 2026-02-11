a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print("Second largest number is:", a)

elif (b >= a and b <= c) or (b <= a and b >= c):
    print("Second largest number is:", b)

else:
    print("Second largest number is:", c)
