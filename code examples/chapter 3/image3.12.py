# A numeric sequence of 1 (inclusive)
# till 10 (exclusive) is requires with
# a step of 0.5. So in the range()
# function, a start of 10 is put in place
# but a finish of 10 * 10 (10 ^ 1 decimal places)
# with a step of 5. If 10 was neede to be reached,
# the step would be added to finish, thus making it 105
for i in range(10, 100, 5):
    print(i / 10) # i / 10 creates the floating point sequence required
