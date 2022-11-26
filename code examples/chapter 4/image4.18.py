# Reversing a list is much better
# with the reverse() method rather
# than with indexing, since it
# does not need to be assigned back
# to a variable
li = [1, 3, 8, 0, 10, 123, 5]
print(li[-1::-1])
print(li)
li.reverse()
print(li)
