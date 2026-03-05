import re

s = input("Enter snake_case string: ")
components = s.split('_')
camel = components[0] + ''.join(x.title() for x in components[1:])
print(camel)