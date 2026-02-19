# 1 example
#Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

# 2 example
#Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))

# 3 example
#Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# 4 example
#Or, use the same function definition to make both functions, in the same program:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
