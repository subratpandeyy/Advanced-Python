ch = input("Enter a character: ").lower()
match ch:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")
    case _:
        print("Consonant")
