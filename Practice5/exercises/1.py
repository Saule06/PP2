import re

s = input("Enter string: ")
if re.fullmatch(r"ab*", s):
    print("Match")
else:
    print("No match")