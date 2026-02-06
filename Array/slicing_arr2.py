# LETS REVERSE ALL THE ELEMENTS

from array import *

val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
reversedArray = val[::-1]
for i in range(0, len(reversedArray)):
    print(reversedArray[i], end=" ")

# sorting an array
print('\n')
arr1 = array('i', [8, 3, 7, 1, 8, 5])
sorted_arr = array('i', sorted(arr1))
print(sorted_arr)


# merging
print('\n')
arr4 = arr1 + val
print(arr4)


# splitting
print('\n')
idx = int(len(arr4)/2)
print(idx)

print(arr4[idx:])
print(arr4[:idx])
