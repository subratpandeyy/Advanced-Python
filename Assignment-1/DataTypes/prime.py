lst = [2, 3, 4, 5, 6, 7, 8, 9, 11]
primes = []
for num in lst:
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
print("Prime Numbers:", primes)
