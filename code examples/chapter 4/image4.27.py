lst = [1, 2, 4, 5, 6]
print(len(lst))

# no size equivalent in base python
t = [[10] * 3, [10] * 3, [10] * 3]
print(t)

a = [*range(1, 11, 2)]
print(a)
print(a[0:3])

t.clear()
print(t)

a.append(5)
print(a)

del a[2] # removes the value of index 2 and deletes it from memory
print(a)

v = a.pop(1)
print(v)

t = [9, 1, 2, 10, 87, 32]
t.sort()
print(t)

a.reverse()
print(a)

count = a.count(5)
print(count)

indexing = a.index(7)
print(indexing)

print(10 in a)
