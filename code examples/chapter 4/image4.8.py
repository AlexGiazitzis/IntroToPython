# from example Image 4.7
List1d = [1, 2, 3, 4, 5]

List2d = [[1, 2, 3], \
          [4, 5, 6]]

List3d = [[[1, 2, 3], \
           [4, 5, 6]], \
          [[7, 8, 9], \
           [10, 11, 12]]]

# Multidimensional list indexing
# using multiple bracket operator pairs

print(List1d[3])
print(List2d[0])
print(List2d[0][2])
print(List3d[1])
print(List3d[1][0])
print(List3d[1][0][2])
