'''
By default, a function must be called with the correct number of arguments.

However, sometimes you may not know how many arguments that will be passed into your function.

*args and **kwargs allow functions to accept a unknown number of arguments.

Arbitrary Arguments - *args
If you do not know how many arguments will be passed into your function, add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly:
'''
# 1 example
#Using *args to accept any number of arguments:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# 2 example
#Accessing individual arguments from *args:

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

# 3 example
#Finding the maximum value:

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))

# 4 example
#Using **kwargs to accept any number of keyword arguments:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# 5 example
#Accessing values from **kwargs:

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

# 6 example
# Combining args and kwargs:
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")
