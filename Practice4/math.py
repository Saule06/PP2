#1
import math

degree = float(input())
radian = math.radians(degree)

print(radian)

#2
h = float(input())
a = float(input())
b = float(input())

area = (a + b) / 2 * h
print(area)

#3
import math

n = int(input())
a = float(input())

area = (n * a * a) / (4 * math.tan(math.pi / n))
print(area)

#4
base = float(input())
height = float(input())

area = base * height
print(area)