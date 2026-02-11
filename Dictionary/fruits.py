fruit={
    "orange":10,
    "apple":20,
    "grapes":30,
    "banana":50
}

for key,values in fruit.items():
    print(key,":",values)
print("-------------------")    
total=sum(fruit.values())
print("Total price of fruits:",total)