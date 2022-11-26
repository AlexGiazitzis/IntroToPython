PS = 0  # Possible combinations

for x in range(0, 41):  # coins of value of 0.5 euro
    for y in range(0, 41):  # coins of value of 1 euro
        for z in range(0, 41):  # coins of value of 2 euros
            for w in range(0, 41):  # coins of value of 5 euros
                syn_plithos_nom = x + y + z + w
                syn_aksia_nom = x * 0.5 + y * 1 + z * 2 + w * 5
                if syn_plithos_nom == 40 and syn_aksia_nom == 40:
                    PS += 1
                    print(f"Combination #{PS}: {x}x0.5E {y}x1E {z}x2E {w}x5E")
print(f"PS = {PS}")
