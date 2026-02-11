num = int(input("Enter a number: "))

if (num % 3 == 0 and num % 7 != 0) or (num % 7 == 0 and num % 3 != 0):
    print("The number is divisible by 3 or 7 but not both")
else:
    print("The conditon is not satisfy")
