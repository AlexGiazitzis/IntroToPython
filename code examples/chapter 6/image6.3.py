file = open("test.txt", 'r')

# Reads all the content of the file as a single string
first = file.read()
print(first)

# Reset the position of the file's pointer
file.seek(0)

# Reads the first line of the file. A line terminates with a newline character.
second = file.readline()
print(second)

# Reads the remaining lines as a list. If called first, it would read all the lines.
third = file.readlines()
print(third)

file.seek(0)

# The file's content can also be accessed using an enhanced for loop
for line in file:
    print(line)

file.close()
