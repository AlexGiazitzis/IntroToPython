import numpy as np
from matplotlib import pyplot as plt

RL = np.arange(1, 101)
V = 10
RS = 10
Rtot = RS + RL
I = V / Rtot
PL = I ** 2 * RL
plt.plot(RL, PL)
plt.grid(True)
plt.xlabel("RL (OHM)")
plt.ylabel("PL (WATT)")
plt.show()
