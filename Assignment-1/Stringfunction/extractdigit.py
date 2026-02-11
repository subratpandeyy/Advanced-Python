s = input("Enter string: ")
digits = ""

for ch in s:
    if ch.isdigit():
        digits += ch

print("Extracted digits:", digits)
