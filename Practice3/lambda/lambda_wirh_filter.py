# 1 examle
#Filter out even numbers from a list:

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# 2 example
nums = [3, 7, 1, 9, 4]
k = 5

result = list(filter(lambda x: x > k, nums))
print(result)
# [7, 9]

# 3 example
nums = [-5, -1, 0, 2, 6]

positive = list(filter(lambda x: x > 0, nums))
print(positive)
# [2, 6]

# 4 example
names = ["Alice", "Bob", "Anna", "Mike"]

a_names = list(filter(lambda n: n.startswith("A"), names))
print(a_names)
# ['Alice', 'Anna']
