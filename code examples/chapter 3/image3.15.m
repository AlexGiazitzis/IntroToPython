arr = 1:10000;
evenNums = 0;
oddNums = 0;

for i = 1:10000
    if mod(arr(i), 2) == 1
        oddNums = oddNums + 1;
        continue
    end
    evenNums = evenNums + 1
end

sum = 0
for i = 1:0.5:100
    sum = sum + i;
end

disp(evenNums)
disp(oddNums)
disp(sum)
