Sum_rice_count = 0
for i in range(1, 65):
    block_rice = 2 ** (i - 1)
    Sum_rice_count += block_rice
print(f"Total rice count: {Sum_rice_count}")
Kg = Sum_rice_count * 1e-4
print(f"Total rice Kg = {Kg}")
tons = Kg / 1e3
print(f"Total rice tons = {tons}")
print(f"The advisor gained {Sum_rice_count} grains of rice that correspond to {tons} tons")

# Using NumPy, it would be possible to change the for loop for a one liner such as:
# Sum_rice_count = np.sum(2 ** (np.arange(1, 65) - 1))
