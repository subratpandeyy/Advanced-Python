s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

print(s2.union(s1))
print(s2.intersection(s1))
print(s2.difference(s1))
print(s2.symmetric_difference(s1))


print("Symbolic Operators")
print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s1^s2)

print(s2|s1)
print(s2&s1)
print(s2-s1)
print(s2^s1)


s3={1,2,"Bulbul",True,3.14}

print(s1.union(s2,s3))
print(s1.intersection(s2,s3))
print(s1.difference(s2,s3))
print(s1.symmetric_difference(s2))

print(s2.union(s1,s3))
print(s2.intersection(s1,s3))
print(s2.difference(s1,s3))
print(s2.symmetric_difference(s3))


print("Using operators")
print(s1|s2|s3)
print(s1&s2&s3)
print(s1-s2-s3)
print(s1^s2^s3)



