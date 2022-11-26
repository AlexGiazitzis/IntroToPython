file1 = open("test.txt")  # assuming the file exists, else raises an error, uncomment to see.
file2 = open("test2.txt", 'w') # whether the file exists or not, doesn't matter. If the latter, Python will create it
file3 = open("test3.txt", "wb")  # creates a file named test3, with the .bin extension, opened for writing binary content.and

file1.close()
file2.close()
file3.close()

print(file2.closed)
