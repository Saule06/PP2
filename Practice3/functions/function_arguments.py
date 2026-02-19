# 1 examle
#A function with one argument:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# 2 example
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# 3 example
#This function expects 2 arguments, and gets 2 arguments::

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# 4 example
'''Positional Arguments
When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:
'''
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")