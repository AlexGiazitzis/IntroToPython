# In order to switch mode on a file, it must be closed and reopened.

with open("test.txt") as f:
    print(f.readlines())

with open("test.txt", 'a') as f:
    f.write("\nHello from Python")

with open("test.txt", 'r') as f:
    for l in f:
        print(l)
    f.seek(0, 0)
    print(f.readline())
