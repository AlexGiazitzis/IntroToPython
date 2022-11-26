import numpy as np

A = np.arange(9).reshape(3, 3)
print("Matrix A =", A)

B = np.array([1, 2, 3])
print("Matrix B =", B)

C = np.arange(3, 6)
print("Matrix C =", C)

D = np.linspace(1, 20, 10)
print("Matrix D =", D)

# vector dot product can be calculated in two ways
print("The dot product of B and C =", B.dot(C), '-', np.dot(B, C))

# point-to-point multiplication
# @ operator is defined by NumPy to work this way
print("Point-to-point multiplication of B and C =", B @ C, '-', np.dot(B, C))

# matrix multiplication
# @ operator and dot() function are 'smart'
# can distinguish between point-to-point and matrix products
print("Matrix multiplication of B and A =", B @ A, '-', B.dot(A))

print("All elements of A squared =", A ** 2)
print("All elements of A multiplied by 3 =", A * 3)
print("All elements of A subtracted 4 -", A - 4)

print("Square root of all elements of C =", np.sqrt(C))
print("Natural logarithm of all elements of B =", np.log(B))
print("Exponential of all elements of C =", np.exp(C))
print("Hyperbolic tangent of all elements of B =", np.tanh(B))
print("Arc tangent of all elements of C =", np.arctan(C))
print("Det of A =", np.linalg.det(A))
