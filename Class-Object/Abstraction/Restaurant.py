from abc import ABC, abstractmethod

class Restaurant(ABC):
    @abstractmethod
    def veg(self, item, payment):
        pass

    @abstractmethod
    def nonveg(self, item, payment):
        pass

class Vegg(Restaurant):
    def veg(self, item, payment):
        print("Ordered item: ", item)
        print("Cost: $", payment)
    def nonveg(self, item, payment):
        pass

class Nonveg:
    def veg(self, item, payment):
        pass
    def nonveg(self, item, payment):
        print("Ordered item: ", item)
        print("Cost: $", payment)
