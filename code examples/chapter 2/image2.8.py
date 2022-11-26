# The int() function can be used with two parameters,
# one being a string and the second being an integer
# which specifies the base that the number the string
# represents is in, so that it can be transformed to 
# decimal base appropriately.
hexString = '0x100'
octString = '0o010'
binString = '0b11000000'
print(int(hexString, 16))
print(int(octString, 8))
print(int(binString, 2))
