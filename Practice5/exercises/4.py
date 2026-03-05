import re

s = input("Enter string: ")
matches = re.findall(r"[A-Z][a-z]+", s)
print(matches)