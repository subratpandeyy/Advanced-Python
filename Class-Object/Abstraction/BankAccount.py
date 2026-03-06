from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    def show_message(self):
        print("Transaction started")

    @abstractmethod
    def withdraw(self, amount):
        pass

class Savings(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance+amount
        print("Savings amount: ", (self.balance))
    
    def withdraw(self, amount):
        self.balance = self.balance-amount
        print("Withdrawn Amount: ", amount)
        print("Remaining Amount: ", (self.balance))
