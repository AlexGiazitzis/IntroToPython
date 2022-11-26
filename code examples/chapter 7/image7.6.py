import numpy as np

A = np.array([1, 2, 3])  # Creating a vector
l = [1, 2, 3]
# Based on linear algebra, the following should produce a vector
# with each element being 3 times the elements of I
print(l * 3)

# Python lists don't produce the proper result, but NumPy arrays do
print(A * 3)
