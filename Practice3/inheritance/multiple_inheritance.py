# 1 example
class Father:
    def skills(self):
        print("Gardening, Driving")

class Mother:
    def skills(self):
        print("Cooking, Painting")

class Child(Father, Mother):
    pass

c = Child()
c.skills()

# 2 example
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Coding")

c = Child()
c.skills()

# 3 example
class Father:
    def __init__(self):
        print("Father constructor")

class Mother:
    def __init__(self):
        print("Mother constructor")

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        print("Child constructor")

c = Child()

# 4 example
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(A):
    def show(self):
        super().show()
        print("C")

class D(B, C):
    def show(self):
        super().show()
        print("D")

d = D()
d.show()
