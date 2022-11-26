hour = 14

# Unorganized conditions may lead to
# unexpected results
if hour >= 0:
    print("Midnight")
elif hour >= 7:
    print("Morning")
elif hour >= 13:
    print("Noon")
else:
    print("Night")
