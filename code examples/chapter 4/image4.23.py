# Using the in operator, it is possible
# to check if a list contains a certain variable/literal
# as an element
intRange = [*range(0, 10)]
print(intRage)
print(10 in intRage)
print(3 in intRange)
print([1, 2, 3] in intRange)
print(12 not in intRange)
intRange.append([3, 4, 5])
print(intRange)
print([3, 4, 5] in intRange)
