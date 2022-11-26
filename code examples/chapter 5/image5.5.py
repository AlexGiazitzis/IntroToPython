# Using functions from other files is
# simply done by importing them with the following line
from functions import *
# the syntax is pretty much as follows
# from file-name import * - to import everything from that file
# from file-name import function1, function2, ... - to import specific functions from that file
# This is a simpler syntax, but can incur Shadowing (explained below).

# Alternatively, another statement can be used to import a file
# import file-name
# this imports everything from the file
# but they are only usable by calling them similarly to methods
# So function1 from file1 would be called as file1.function1(params)
# This kind of importing does make the syntax a bit uglier but
# allows the developers to write functions without the shadowing issue.

# Shadowing: when a function/variable is named the same as an existing function/variable,
# it shadows the latter making it unusable1

arr = [1, 2, 3, 4]
print(summ(arr))
print(comp(arr[2], arr[3]))
