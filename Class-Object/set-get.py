class stu:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, m):
        self.__marks = m

    def get_marks(self):
        print(self.__marks)

s = stu(100)
s.set_marks(20)
s.get_marks()

