import numpy as np
from array import *

np1 = np.array([20, 30, 40, 50])
np2 = np.array([60, 70, 80])

print(np1)
print(np2)

# accessing
print('\n')
np1[3]

print('\n')
np2[2]

# traversing
print('\n')
for i in np2:
    print(i, end=" ")


# insertion
print('\n')
np3 = np.insert(np2, 2, 75)
print(np3)


# deletion
print('\n')
np3 = np.delete(np3, 2)
print(np3)

# updation
print('\n')
np1[0] = 10
print(np1)


# sorting
print('\n')
np5 = np.array([5, 4, 6, 7, 2, 3, 1])
print(np5)
np5 = np.sort(np5)
print(f"sorted array = {np5}")

# merging numpy arrays
print('\n')
np7 = np.concatenate((np1, np5))
print(np7)
# output : [10 30 40 50  1  2  3  4  5  6  7]


# Splitting
print('\n')
split1, split2, split3 = np.array_split(np7, 3)
print(f"\n {split1}")
print(f"\n {split2}")
print(f"\n {split3}")
