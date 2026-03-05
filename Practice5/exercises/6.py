import re

s = input("Enter string: ")
result = re.sub(r"[ ,\.]", ":", s)
print(result)