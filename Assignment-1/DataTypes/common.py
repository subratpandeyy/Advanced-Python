l1=[1,2,3,4,5]
l2=[3,4,5,6,7]

comman=[]
for item in l1:
    if item in l2:
        comman.append(item)
        
print("Common elements are:",comman)