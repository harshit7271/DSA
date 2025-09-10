# MISSING NUMBERS
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        desired_sum = n*(n+1)//2
        real_sum = sum(nums)
        return desired_sum - real_sum
    
# Example usage:
nums = [3, 0, 1]
solution = Solution()
print(solution.missingNumber(nums))


# Maximum consecutive ones
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0
        for i in nums:
            if i == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count
# Example usage:
nums = [1, 1, 0, 1, 1, 1]
solution = Solution()   
print(solution.findMaxConsecutiveOnes(nums))

# single number
class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
    
# Example usage:
nums = [4, 1, 2, 1, 2]
solution = Solution()
print(solution.singleNumber(nums))

      

        