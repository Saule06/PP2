import re

s = input("Enter string: ")
if re.fullmatch(r"ab{2,3}", s):
    print("Match")
else:
    print("No match")