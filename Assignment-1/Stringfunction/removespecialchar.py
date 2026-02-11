s = input("Enter a string: ")
result = ""
for ch in s:
    if ch.isalnum() or ch == " ":
        result += ch

print("After removing special characters:", result)
