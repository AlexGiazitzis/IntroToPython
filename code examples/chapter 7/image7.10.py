import numpy as np

A = np.arange(9).reshape(3, 3)

print(A)
print(A[1, 2])
print(A[0:3, 1])  # second column of A
print(A[0:3, 0:1])  # first column of A, in vector form
print(A[0:2, 0:2])  # sub-matrix of A
