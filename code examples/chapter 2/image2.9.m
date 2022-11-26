% Giving and getting input to/from the user
disp('Hello world!')

var = input('Enter an expression: ')

stringNum = input('Enter a number: ', 's')

% Transforming a string to a number...
numFrom String = str2num(stringNum)

disp(stringNum * 3)

# and then to binary representation.
disp(['The binary representation of ' ...
num2str(numFromString * 3) ' is: '...
dec2bin(numFromString * 3)])
