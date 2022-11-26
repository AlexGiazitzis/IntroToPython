function s = summ(lst, index)
arguments % making index optional
    lst (:, :, 1) {mustBeNumeric}
    index (1, 2) uint8 = [1, 1]
end
s = 0;
for i = index(1):size(lst, 1)
    for j = index(2):size(lst, 2)
        s = s + lst(i, j);
    end
end

% Copy the following to the command window once the above function is saved to a separate file.

t = 1:0.5:100;
summ(t)
summ(t, [1, 50])
