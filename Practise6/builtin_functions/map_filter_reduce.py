from functools import reduce
nums = []

for i in range(1 , 11):
    nums.append(i)

#map
squared = list(map(lambda x: x**2 , nums))

#filter filters only variables that satisfy lambda func
evens = list(filter(lambda x : x % 2 == 0 , nums))


#reduce (saves everything by the logic written in anonymous func in the variable we присвоили) 
product = reduce(lambda x , y : x + y , nums)


print(f"original nums: {nums}")
print(f"squared: {squared}")
print(f"evens: {evens}")
print(f"product: {product}")