def fib_non_recursive(N):
    if N == 0:
        return 1
    elif N == 1:
        return [1, 1]
    else:
        f = [1, 1]
        for i in range(2, N):
            f.append(f[i - 2] + f[i - 1])
        return f
