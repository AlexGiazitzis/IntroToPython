from matplotlib import pyplot as plt

RL = list(range(1, 101))
V = 10
RS = 10
Rtot = [RS + RLi for RLi in RL]  # this is called a list comprehension
I = [V / Rtoti for Rtoti in Rtot]
PL = [Ii ** 2 * RLi for Ii, RLi in zip(I, RL)]
plt.plot(RL, PL)
plt.grid(True)
plt.xlabel("RL (OHM)")
plt.ylabel("PL (WATT)")
plt.show()
