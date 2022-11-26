def summ(array, index=0):
    summ = 0
    # There is a better alternative for the following for loop
    # which utilizes list slicing that is more pythonic to use:
    #for elem in array[index:]:
    #   summ += elem
    for i in range(index, len(array)):
        summ += array[i]
    return summ

arr = [1, 2, 3, 4]
print(summ(arr))
print(summ(arr, 2))
