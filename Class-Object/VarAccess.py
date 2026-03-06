class VarAccess:
    def __init__(self, name):
        self.name = name

    def dis(self):
        print(self.name)

V = VarAccess("Subrat")
print(V.name)

# deleting variable name
del V.name

