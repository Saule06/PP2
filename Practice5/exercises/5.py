import re

s = input("Enter string: ")
if re.fullmatch(r"a.*b", s):
    print("Match")
else:
    print("No match")