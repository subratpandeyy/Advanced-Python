choice = input("Enter an alphabet: ").lower()
match choice:
    case 'a'|'e'|'i'|'o'|'u':
        print("Vowel")
    case _:
        print("Consonant")