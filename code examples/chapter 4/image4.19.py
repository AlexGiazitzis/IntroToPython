# Counting how many elements are of the same value
# in a list can be easily be performed with a for loop
lst = [1, 1, 1, 2, 3, 4, 2, 4, 5]
counter = 0
for elem in lst:
    if elem == 1:
        counter += 1
print(counter)
