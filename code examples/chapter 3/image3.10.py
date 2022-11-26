data = ""

# The continue statement forces the construct
# to move on to the next iteration, skipping
# all statements and expressions beneath it.
# Whilst the break statement, makes the 
# construct stop looping, even if it's condition
# has not yet become false, exiting the loop's body
# and moving on from it.
# Both statements can be used with both while and
# for statements
while data != "Done":
    data = input()
    if data == "skip":
        print("Iteration skipped.")
        continue
    print("Data inputted was:", data)
    if data == "break":
        printf("Loop exited.")
        break
