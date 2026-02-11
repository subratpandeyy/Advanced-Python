lst = [1, 2, 2, 3, 4, 1, 2, 3]

frequency = {}

for item in lst:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1


print("Frequency of elements:")
for key, value in frequency.items():
    print(key, ":", value)