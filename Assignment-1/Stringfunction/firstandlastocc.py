s = input("Enter string: ")
ch = input("Enter character to find: ")

first = s.find(ch)
last = s.rfind(ch)

print("First occurrence:", first)
print("Last occurrence:", last)
