try:
    data = open("data.txt")

except FileNotFoundError as e:
    print(e)
