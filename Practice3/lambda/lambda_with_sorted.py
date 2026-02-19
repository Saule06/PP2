# 1 example
nums = [-10, 3, -2, 5]

result = sorted(nums, key=lambda x: abs(x))
print(result)
# [-2, 3, 5, -10]


# 2 example
#Sort strings by length:

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# 3 example
pairs = [(1, 3), (4, 1), (2, 2)]

result = sorted(pairs, key=lambda x: x[1])
print(result)
# [(4, 1), (2, 2), (1, 3)]

# 4 example
scores = {"Alice": 90, "Bob": 75, "Charlie": 85}

result = sorted(scores.items(), key=lambda item: item[1])
print(result)
# [('Bob', 75), ('Charlie', 85), ('Alice', 90)]
