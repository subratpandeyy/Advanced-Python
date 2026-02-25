class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("My name is ",self.name," and I am ",self.age," years old!")

    def greet():
        print("Good morning")

S = Student
S1 = Student("Subrat", 20)
print("Object Created Successfully")
S1.display()
S.greet()
