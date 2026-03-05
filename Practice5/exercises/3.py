import re

s = input("Enter string: ")
matches = re.findall(r"[a-z]+_[a-z]+", s)
print(matches)