data = "0"
counter = -1 # start from -1 due to stopping condition counting as an iteration as well
mean = 0
# Using a while statement, one can loop over an unknown amount of times
# as long as the condition evaluates to true
while data != "Done":
    mean += float(data)
    counter += 1
    data = input()

print("Number of iterations completed:", counter)
print("Mean value of all inputted values:", mean / counter)
