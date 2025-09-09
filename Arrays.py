# LARGEST ELEMENT IN AN ARRAY

class Solution:
    def largest(n:int, arr:list[int]) -> int:
        max_val = arr[0]
        for i in range(1, n):
            if arr[i] > max_val:
                max_val = arr[i]
        return max_val
# Example usage:
# n = 5
arr = [1, 2, 3, 4, 5]
print(Solution.largest(len(arr), arr)) 


# second largest element in an array without sorting

class Solution:
    def secondLargest(n:int, arr1:list[int]) -> int:
        largest = second_largest = -1

        for i in arr1:
            if i > largest:
                second_largest = largest
                largest = i
            elif i > second_largest and i != largest:
                second_largest = i

        return second_largest
    # Example usage:
arr1 = [1, 2, 3, 4, 5]
print(Solution.secondLargest(len(arr1), arr1))


# CHECK IF ARRAY IS SORTED OR NOT

class Solution:
    def isSorted(n:int, arr2:list[int]) -> bool: 
        n = len(arr2)
        if n == 0 or n == 1:
            return True
        count = 0
        for i in range(n):
            if arr2[i] > arr2[(i + 1) % n]:
                count += 1
        return count <= 1
# Example usage:
arr2 = [1, 2, 3, 4, 5] 
print(Solution.isSorted(len(arr2), arr2)) 


# Remove Duplicate From Sorted Array

class Solution:
    def removeDuplicates(n:int, arr3:list[int]) -> int:
        if not arr3:
            return 0
        k = 1
        for i in range(1,len(arr3)):
            if arr3[i] != arr3[k-1]:
                arr3[k] = arr3[i]
                k += 1
        return k
# Example usage:
arr3 = [1, 1, 2, 2, 3]
print(Solution.removeDuplicates(len(arr3), arr3))  \


# Rotated Array (Left or Right)  ---  
    
        ## TRICK (1) Reverse the whole array (0, n-1)
        ## TRICK (2) Reverse the first k elements  (0, k-1)
        ## TRICK (3) Reverse the remaining n-k elements (k, n-1)

 # Right Rotation
class Solution:
    def rotate(arr4:list[int], k: int) -> list[int]:
        n = len(arr4)
        k = k % n

        def reverse(start: int, end: int) -> None:
                while start < end:
                    arr4[start], arr4[end] = arr4[end], arr4[start]
                    start += 1
                    end -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        return arr4 

# Example usage:
arr4 = [1, 2, 3, 4, 5]  
k = 2
print(Solution.rotate(arr4, k))
# Output: [3, 4, 5, 1, 2]  

# Left Rotation -----
            ##TRICK (1) Reverse the first k elements  (0, k-1)
            ##TRICK (2) Reverse the remaining n-k elements (k, n-1)
            ## RICK (3) Reverse the whole array (0, n-1)
class Solution:
    def rotateLeft(arr5:list[int], k: int) -> list[int]:
        n = len(arr5)
        k = k % n

        def reverse(start: int, end: int) -> None:
                while start < end:
                    arr5[start], arr5[end] = arr5[end], arr5[start]
                    start += 1
                    end -= 1
        reverse(0, k - 1)
        reverse(k, n - 1)
        reverse(0, n - 1)
        return arr5
# Example usage:
arr5 = [1, 2, 3, 4, 5]
k = 2
print(Solution.rotateLeft(arr5, k))
# Output: [3, 4, 5, 1, 2]


# MOVE ZEROES TO END OF ARRAY
class Solution:
    def moveZeroes(arr6:list[int]) -> list[int]:
        n = len(arr6)
        j =0
        for i in range(n):
            if arr6[i] != 0:
                arr6[j], arr6[i] = arr6[i], arr6[j]
                j += 1

        return arr6
# Example usage:
arr6 = [0, 1, 0, 3, 12]
print(Solution.moveZeroes(arr6))
# Output: [1, 3, 12, 0, 0]  


# BINARY SEARCH

class Solution:
    def searchInSorted(self,arr,N,K):
        p,q = 0,N-1
        while p<=q:
            mid = p+(q-p)//2
            if arr[mid]==K:
                return 1
            elif arr[mid]<K:
                 p = mid+1
            else:
                q = mid-1
        return -1
# Example usage:
arr7 = [1, 2, 3, 4, 5]
K = 3
print(Solution().searchInSorted(arr7, len(arr7), K))
# Output: 1 (Element found)


# UNION OF TWO SORTED ARRAYS
# Two methods: 1. Using Set  2. Using Two Pointers
# Method 1: Using Set
class Solution:
    def unionSet(arr1 : list[int], arr2: list[int]) -> list[int]:
        set1 = set(arr1)
        set2 = set(arr2)
        union = set1.union(set2)
        return sorted(list(union))
    
# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
print(Solution.unionSet(arr1, arr2))
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Method 2: Using Two Pointers
class Solution:
    def unionTwoPointers(arr1 : list[int], arr2: list[int]) -> list[int]:
        i, j = 0, 0
        union = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if not union or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1
            else:
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
                j += 1
        while i < len(arr1):
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        while j < len(arr2):
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        return union
# Example usage:
arr1 = [1, 2, 3, 4, 5]  
arr2 = [4, 5, 6, 7, 8]
print(Solution.unionTwoPointers(arr1, arr2))
# Output: [1, 2, 3, 4, 5, 6, 7, 8]










   
     

    


             










        









