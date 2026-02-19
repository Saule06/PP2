# 1 example
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):  # override parent method
        print("Woof!")

a = Animal()
d = Dog()

a.speak()  # Some sound
d.speak()  # Woof!


# 2 example
class Dog(Animal):
    def speak(self):
        super().speak()  # call parent method
        print("Woof!")   # add child behavior

d = Dog()
d.speak()
# Some sound
# Woof!

# 3 example
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

class Bike(Vehicle):
    def move(self):
        print("Bike is pedaling")

v = Vehicle()
c = Car()
b = Bike()

v.move()  # Vehicle is moving
c.move()  # Car is driving
b.move()  # Bike is pedaling

# 4 example
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # call parent constructor
        self.breed = breed

d = Dog("Rex", "Labrador")
print(d.name, d.breed)  # Rex Labrador
