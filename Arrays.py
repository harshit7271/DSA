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



