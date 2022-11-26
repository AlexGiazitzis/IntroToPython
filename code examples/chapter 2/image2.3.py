# Code example of how input() returns string values
# that have to be transformed in order to be used properly.
x = input()
y = input()
#print(x * y) # commented out as it would raise an error. uncomment and run to see.

xNum = int(x) # or float(x)/float(y), depending on what will be inputted
yNum = int(y)
print(xNum * yNum)

z = input()
zNum = float(z) # or int(z), same as above
print(zNum * 2)
