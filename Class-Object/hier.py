class school:
    def __init__(self):
        print("School")
class parent(school):
    def __init__(self):
        super().__init__()
        print("Parent")
class teacher(school):
    def __init__(self):
        super().__init__()
        print("Teacher")
p = parent()
t = teacher()
