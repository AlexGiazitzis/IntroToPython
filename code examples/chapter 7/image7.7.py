import numpy as np
from datetime import datetime as dt

L = [1, 2, 3]
B = np.array([1, 2, 3])

T = 10_000  # amount of iterations

t1 = dt.now()
for t in range(T):
    for ind in range(len(L)):
        L[ind] = L[ind] * 3
dt1 = dt.now() - t1
print("List product implementation time:", dt1.total_seconds())

t2 = dt.now()
for t in range(T):
    B = B * 3
dt2 = dt.now() - t2
print("NumPy product implementation time:", dt2.total_seconds())
print("Time ratio:", dt1.total_seconds() / dt2.total_seconds())
