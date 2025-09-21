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

# Longest subarray with sum k 

class Solution:
    def maxSubArrayLen(self, nums, k):
        sum_index_map = {}
        current_sum = 0
        max_length = 0
        
        for i in range(len(nums)):
            current_sum += nums[i]
            
            if current_sum == k:
                max_length = i + 1
            
            if (current_sum - k) in sum_index_map:
                max_length = max(max_length, i - sum_index_map[current_sum - k])
            
            if current_sum not in sum_index_map:
                sum_index_map[current_sum] = i
        
        return max_length
# Example usage:
nums = [1, -1, 5, -2, 3]
k = 3
solution = Solution()
print(solution.maxSubArrayLen(nums, k))

# PLUS ONE
class Solution:
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits
    
# Example usage:
digits = [1, 2, 3]
solution = Solution()   
print(solution.plusOne(digits))

# Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_profit:
                max_profit = i - min_price
        
        return max_profit



      

        