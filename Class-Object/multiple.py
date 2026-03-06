class dad:
    def __init__(self):
        print("Dad")
class mom:
    def __init__(self):
        print("Mom")
        super().__init__()
class son(mom, dad):
    def __init__(self):
        super().__init__()
        print("Son")

s = son()
