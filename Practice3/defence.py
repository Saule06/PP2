class Human:
    def __init__(self, role):
        self.role = role


class Person(Human):
    def __init__(self, name, age):
        super().__init__("Person")
        self.name = name
        self.age = age

    def display(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old.")


class Student(Human):
    def __init__(self, grade):
        super().__init__("Student")
        self.grade = grade

    def display(self):
        print(f"I am a student in grade {self.grade}.")


class Doctor(Human):
    def __init__(self, h_name, speciality):
        super().__init__("Doctor")
        self.h_name = h_name
        self.speciality = speciality

    def display(self):
        print(f"I am a doctor at {self.h_name}, speciality: {self.speciality}.")
        
p = Person("Saule", 19)
s = Student(10)
d = Doctor("BSMP", "Doctor")

objects = [p, s, d]

for obj in objects:
    obj.display()
       