l1=[34,5,67,9,2,3,90,35]
even=0
odd=0
for i in l1:
    if i%2==0:
        even+=1
    else:
        odd+=1

print("The even number is:",even)
print("the odd number is:",odd)