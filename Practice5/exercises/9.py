import re

s = input("Enter string: ")
result = re.sub(r'([A-Z])', r' \1', s).strip()
print(result)