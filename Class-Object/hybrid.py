class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_student(self):
        print(f"Name     : {self.name}")
        print(f"Roll No. : {self.roll_no}")

class AcademicMarks(Student):
    def __init__(self, academic_marks):
        self.academic_marks = academic_marks

    def display_academic_marks(self):
        print(f"Academic Marks : {self.academic_marks}")

class SportsMarks(Student):
    def __init__(self, sports_marks):

        self.sports_marks = sports_marks

    def display_sports_marks(self):
        print(f"Sports Marks   : {self.sports_marks}")

class FinalReport(AcademicMarks, SportsMarks):
    def __init__(self, academic_marks, sports_marks):
       AcademicMarks.__init__(self, academic_marks)
       SportsMarks.__init__(self, sports_marks)

    def display_report(self):
        print("\n--- Final Report ---")
        print("======================")
        self.display_student()
        self.display_academic_marks()
        self.display_sports_marks()
        total = self.academic_marks + self.sports_marks
        print(f"Total Marks    : {total}")

student1 = FinalReport("Subrat Pandey", "23CSE514", 80, 15)
student1.display_report()

