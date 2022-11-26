import array as a

int_array = a.array('i')
char_array = a.array('u')
float_array = a.array('f')

int_array2 = a.array('i', [1, 2, 3, 4])
print(int_array)
print(int_array.typecode)
print(int_array.itemsize)
print(int_array.tolist())

char_array.fromlist(['a', 'b', 'c', 'd'])
for i in char_array:
    print(i)

print(char_array)

char_list = char_array.tolist()
print(char_list)
