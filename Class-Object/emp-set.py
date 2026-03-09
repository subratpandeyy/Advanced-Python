class Employee:
    def __init__(self, name, dept, sal):
        self.name = name
        self._dept = dept
        self.__sal = sal

    def set_sal(self, update):
        self.__sal = update

    def get_sal(self):
        print(self.__sal)

class Manager(Employee):
    def update_sal(self, salary):
        self.set_sal(salary)

E = Manager("Subrat", "CSE", 1000)

E.update_sal(3000)
E.get_sal()
