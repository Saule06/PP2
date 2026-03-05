import re

s = input("Enter string: ")
parts = re.split(r'(?=[A-Z])', s)
print(parts)