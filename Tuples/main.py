t1=("Aditya","Sagar",True,False,1,2,143,3.5)
l=list(t1)
print(l.append(45))
t1=tuple(l)
print(t1)
print(type(t1))
print(t1.count(1))
print(t1.index("Sagar"))


a = 10
b = 20
c = 30

t = a, b, c
print(t)

x, y, z = t
print(x)
print(y)
print(z)

t1 = (1, 2, 3)
t2 = (4, 5, 6)

t3 = t1 + t2
print(t3)


