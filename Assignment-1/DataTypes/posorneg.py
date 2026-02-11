lst=[23,34,-90,-74,9,-1,44,35,66,-23]

positive=[]
neagitive=[]

for item in lst:
    if item>=0:
        positive.append(item)
    else:
        neagitive.append(item)
print("the postive number are",positive)
print("the negative number are",neagitive)        