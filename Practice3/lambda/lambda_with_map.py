# 1 example
#Double all numbers in a list:

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# 2 example
nums = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, nums))
print(squares)
# [1, 4, 9, 16]

# 3 example
nums = [10, 20, 30]
k = 5

result = list(map(lambda x: x + k, nums))
print(result)
# [15, 25, 35]

# 4 example
words = ["python", "map", "lambda"]

lengths = list(map(lambda w: len(w), words))
print(lengths)
# [6, 3, 6]