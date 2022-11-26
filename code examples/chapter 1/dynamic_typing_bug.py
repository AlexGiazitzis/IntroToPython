"""
A really basic program that demonstrates the dynamic typing approach
Python offers. Age starts as a String, due to how the input() function works
but then is turned into an integer using the int() function, thus not being allowed
to be concatenated with other strings. This bug can be fixed by wrapping age with the str()
function, using f-strings or the format() method of String.
"""

age = input("Enter you age: ")
print("You entered " + age + " years old")
age = int(age)
age += 10
print("You will be " + age + " years old in 10 years")