class Book:
    def __init__(self,title, desc, price):
        self.title = title
        self.desc = desc
        self.price = price

    def display(self):
        print(self.title)
        print(self.desc)
        print(self.price)

B = Book("NCERT", "Chemistry 12th std", 200)
B.display()
