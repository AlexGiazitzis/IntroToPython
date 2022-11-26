# List slicing can also be performed
# with only one operand in the syntax start:end
# or either the start or end and the step
# in the syntax start:end:step
intList = [*range(0, 10)]
endList = intList[4:]
beginList = intList[:4]
print(intList)
print(endList)
print(beginList)
