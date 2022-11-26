def ask1_1f(val1, val2, val3, val4):
    PS = 0
    for x in range(0, 41):
        for y in range(0, 41):
            for z in range(0, 41):
                for w in range(0, 41):
                    syn_plithos_nom = x + y + z + w
                    syn_aksia_nom = x * 0.5 + y * 1 + z * 2 + w * 5
                    if syn_plithos_nom == 40 and syn_aksia_nom == 40:
                        PS += 1
                        print(f"Combination #{PS}: {x}x0.5E {y}x1E {z}x2E {w}x5E")
    return PS
