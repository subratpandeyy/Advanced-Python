class Bank:
    def __init__(self, name, branch, amount):
        self.name = name
        self._branch = branch
        self.__amount = amount

    def display_name(self):
        print(self.name)

    def display_branch(self):
        print(self._branch)

    def display_amount(self):
        print(self.__amount)

B = Bank("BOI", "Gunupur", 10000)
B.display_name()
B.display_branch()
B.display_amount()

#name mangling
print(B._Bank__amount)
