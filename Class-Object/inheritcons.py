class parent:
    def __init__(self):
        print("Parent")

class child(parent):
    def __init__(self):
        super().__init__()
        print("Child")

c = child()
