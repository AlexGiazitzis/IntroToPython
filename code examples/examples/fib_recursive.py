def fib_recursive(N):
    y = []
    for i in range(0, N):
        y.append(my_fibo(i))
    return y

def my_fibo(i):
    if i == 0 or i == 1:
        return 1
    else:
        return my_fibo(i - 2) + my_fibo(i - 1)
