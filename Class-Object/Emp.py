class Employee:
    def __init__(self, name, dept, sal):
        self.name = name
        self.dept = dept
        self.sal = sal
    
    def display(self):
        print("Employee name: ",self.name)
        print("Employee department: ", self.dept)
        print("Employee Salary: ", self.sal)

E = Employee("Subrat", "CSE", 50000)
E.display()
