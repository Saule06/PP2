# 1 example
class Student:
    school = "High School"   # class variable

# 2 example
class Student:
    school = "High School"   # class variable

    def __init__(self, name):
        self.name = name     # instance variable

# 3 example
class Counter:
    count = 0   # class variable

    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
c = Counter()

print(Counter.count)  # 3

# 4 example
class Car:
    wheels = 4   # class variable

    @classmethod
    def change_wheels(cls, num):
        cls.wheels = num

print(Car.wheels)  # 4
Car.change_wheels(6)
print(Car.wheels)  # 6
