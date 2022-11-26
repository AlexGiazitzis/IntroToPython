import os
print(os.listdir()) # shows how functions.py is in the working directory

import functions as fncs

# Using list comprehension to generate proper sequence
# as range() step parameter can't be float
# comprehensions are expressions that allow simple but powerful one-liners
# such as creating a list/dict/set from another iterable like the one below
lst = [x * 0.5 for x in range(2, 201)]

print(fncs.summ(lst))
print(fncs.summ(lst, 50))
