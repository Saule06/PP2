'''
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

'''
# 1 example
#Create a class named MyClass, with a property named x:

class MyClass:
  x = 5

# 2 example
#Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)

# 3 example
#Create three objects from the MyClass class:

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# 4 example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 20)
p2 = Person("Bob", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)
