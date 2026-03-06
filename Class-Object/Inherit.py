class Parent:
    def parent_method():
        print("Parent method")

class child(Parent):
    def child_method():
        print("Child class")

class grandchild(child):
    def grand_method():
        print("Grand Child")

c = grandchild
c.grand_method()
c.child_method()
c.parent_method()
