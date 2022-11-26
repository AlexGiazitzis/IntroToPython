password = "Strong password!"

# This time, if the password IS NOT the value "Strong password!"
# then the first print will be executed, but if it IS that value,
# the second print statement will be executed
if password != "Strong password!":
    print("Wrong password. Access denied.")
else:
    print("Password is correct! Access granted!")
