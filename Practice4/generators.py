#1
def squares_up_to(n):
    for i in range(1, n + 1):
        yield i * i

n = int(input())
for s in squares_up_to(n):
    print(s)

#2
n = int(input())

evens = (str(i) for i in range(0, n + 1) if i % 2 == 0)
print(",".join(evens))

#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in divisible_by_3_and_4(n):
    print(num)

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for value in squares(3, 7):
    print(value)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for num in countdown(n):
    print(num)