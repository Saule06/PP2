'''
A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code repetition.

'''
# 1 example
def my_function():
  print("Hello from a function")
''' 
This creates a function named my_function that prints "Hello from a function" when called.
The code inside the function must be indented. Python uses indentation to define code block
'''
# 2 example
#To call a function, write its name followed by parentheses:
def my_function():
  print("Hello from a function")

my_function()

# 3 example
#With functions - reusable code:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# 4 example
#A function that returns a value:

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)