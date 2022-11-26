mean = 0
data = ""
# A for loop allows us to iterate over a set of code a specific
# amount of times.
for i in range(0, 10): # will do 10 iterations, start at 0, finish at 9
    data = input()
    mean += float(data)

mean /= (i + 1)
print("The average of 10 inputted values is:", mean)
