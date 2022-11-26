lst = [1, 2, 4, 5, 6]; % declaration
length(lst); % matrix length (biggest dimension)
size(lst) # matrix's dimensions (as a matrix)

% generate a matrix of zeros
% add the value to all elements
t = zeros(3, 3) + 10 % matrix filled with 10

a = 1:2:10 % consecutive values
a(1:3) % slicing
t = [] % clearing
a = [a 5] % "appending"/concatenating

% inserting isn't immediately possible
% extension can be achieved through concatenation
a(3) = [] % removing element

% "pop" value
v = a(2)
a(2) = []

t = rand(1, 10);
sort(t) % sorting

a = a(end:-1:1) % reversing

count = sum(ismember(a, 5))
indexing = find(a == 7, 1)

% element in matrix
ismember(10, a)
