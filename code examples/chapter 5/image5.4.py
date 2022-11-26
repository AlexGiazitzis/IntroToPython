# A return statement does not have to be
# the last statement in a function. It can
# even not exist.
def comp(a, b):
    if a > b:
        return True
    elif a < b:
        return False
    else:
        return None

a = comp(1, 1)
print(a == None)
print(comp(1, 2))
print(comp(10, 4))
