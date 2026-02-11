book={
    "name":"all of us are dead",
    "author":"jong-kwan",
    "price":250,
    "publisher":"netflix",
    "pages":350,
    "rating":8.9,
    "genre":"horror",
    "language":"korean",
    "year":2022

}
for i in book.values():
    print(i)


for key,value in book.items():
    print(key,":",value)    



if "language"=="korean":
    book.pop("language")
else:
    print("Enter the another criteria")    

 