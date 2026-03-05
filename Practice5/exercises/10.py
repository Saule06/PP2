import re

s = input("Enter camelCase string: ")
snake = re.sub(r'([A-Z])', r'_\1', s).lower()
if snake[0] == '_':  # remove leading underscore if exists
    snake = snake[1:]
print(snake)