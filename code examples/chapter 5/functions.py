# Production UNSAFE, don't use.

def summ(array, index=0):
    """
    A rought implementation of the sum() built-in function.
    These type of comments are called docstrings and are what
    Python prints when using the help() function.
    """
    summ = 0
    for elem in array[index:]:
       summ += elem
    return summ

def comp(a, b):
    """
    A simple function that compares two numbers and returns an appropriate value.
    """
    if a > b:
        return True
    elif a < b:
        return False
    else:
        return None
