import math as m

def my_exp_func(x):
    FIXED = m.exp(x)
    S = 0
    i = 0
    term = x ** i / m.factorial(i)
    S += term
    while abs(S - FIXED) >= 1e-5:
        i += 1
        term = x ** i / m.factorial(i)
        S += term
    return i
