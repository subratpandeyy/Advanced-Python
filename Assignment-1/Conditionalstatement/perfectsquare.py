import math

num=int(input("Enter a number: "))
root=int(math.sqrt(num))

if root*root==num:
    print("Perfect Square")
else:
    print("Not a perfect square")    