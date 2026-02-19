# 1 example
#Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# 2 example
#Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass

# 3 example
#Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")
x.printname()

# 4 example
# Parent class
class Animal:
    def speak(self):
        print("Some sound")

# Child class
class Dog(Animal):
    pass

dog = Dog()
dog.speak()  # Some sound
