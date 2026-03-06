class Bank:
    def interest(self):
        print("Bank")

class savings(Bank):
    def interest(self):
        print("8% interest")

class current(Bank):
    def interest(self):
        print("10% interest")

class fixed(Bank):
    def interest(self):
        print("5% interest")

f = fixed()
f.interest()
c = current()
c.interest()
s = savings()
s.interest()

b = Bank()
b.interest()
