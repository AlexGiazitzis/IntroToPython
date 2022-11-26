# Using the with keyword to open a file,
# makes the I/O process safer, as manually
# closing the file after writing something to it
# could corrupt it as it could close at the midst of writing
# With the with statement, the file closes only once every
# operation has ended.
with open("test.txt", 'r') as f:
    for l in f:
        print(l)
print(f.closed)
