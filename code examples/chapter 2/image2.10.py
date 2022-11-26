# Giving and getting input from/to the user
print('Hello world!')
# the eval() function evaluates the statement/expression
# given to it as a parameter, essentially working like
# the interactive shell
var = eval(input('Enter an expression: '))
print(var)
stringNum = input('Enter a number: ')
print(stringNum)
# Transforming a string to an int and back to string
# using the binary representation.
numFromString = int(stringNum)
print(numFromString * 3)
print('The binary representation of', \
      numFromString * 3, 'is:', bin(numFromString * 3))
