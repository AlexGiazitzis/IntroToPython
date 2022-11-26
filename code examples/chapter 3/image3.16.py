# arr uses range from 1 to 10001
# due to the latter being excluded
arr = [*range(1, 10001)] # equivalent to list(range(1, 10001))
evenNums = 0
oddNums = 0

for i in range(0, 10000):
    if arr[i] % 2 == 1:
        oddNums += 1
        continue
    evenNums += 1

summ = 0 # summ instead of sum so there is no shadowing with the function sum()
for i in range(10, 1005, 5): # numerical sequence from 1 to 100 with a step of 0.5
    summ += (i * 0.1)

print(evenNums)
print(oddNums)
print(summ)
