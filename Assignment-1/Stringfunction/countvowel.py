s = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for ch in s:
    if ch in vowels:
        count += 1

print("the total vowel count is :", count)
