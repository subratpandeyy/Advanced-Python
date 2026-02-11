num = int(input("Enter a number: "))
product = 1
while num > 0:
    digit = num % 10
    product *= digit
    num //= 10
print("Product of digits:", product)
