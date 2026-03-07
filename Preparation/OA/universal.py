from typing import List


def reverseNum(num):
    ans = 0
    while num > 0:
        ans = ans*10 + num % 10    # remainder = num % 10
        num = num//10
    return ans


print(reverseNum(1234))


data = [4, 6, 2, 3, 1, 7, 5]

# slicing method
"""
reversed_data = data[::-1]
print(reversed_data)
"""
n = len(data)
reversed_data = []

for i in range(n-1, -1, -1):
    reversed_data.append(data[i])
print(f'{reversed_data} is the reversed list')


"""
n = len(data) - 1
reversed_data2 = []
while n >= 0:
    reversed_data2.append(data[n])
    n -= 1
print(reversed_data2)

"""

# reverse a string


class solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1

# check palindrome


def is_palindrome(s):
    return s == s[::-1]

# other way


def is_palindrome2(s):
    if not s:
        return True

    s = s.lower().replace(" ", "")

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# two sum

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# max subarray sum

def maxSubArray(self, nums):
    n = len(nums)
    maxi = float("-inf")
    for i in range(0, n):
        total = 0
        for j in range(i, n):
            total = total + nums[j]
            maxi = max(maxi, total)
    return maxi

# other way


def maxSubArrar2(self, nums):
    n = len(nums)
    maxi = float("-inf")
    total = 0

    for i in range(0, n):
        total = total + nums[i]
        maxi = max(maxi, total)
        if total < 0:
            total = 0
    return maxi


# move zeros

def moveZeros(self, nums: List[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[i]
            j += 1

# best time to buy and sell stock


def maxProfit(self, prices: List[int]) -> int:
    buy = prices[0]
    max_profit = 0

    for price in prices:
        if price < buy:
            buy = price
        else:
            max_profit = max(max_profit, price - buy)
    return max_profit


# Find the missing number

def missingNumber(self, nums: List[int]) -> int:
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return len(nums)

# or


def missingNum(self, nums: List[int]) -> int:
    return len(nums)*(len(nums)+1)//2 - sum(nums)


# first unique character in a string
class Solution(object):
    def firstUniqChar(self, s):
        j = {}  # create a dict to store frequency
        for x in s:
            j[x] = j.get(x, 0) + 1
        for i, x in enumerate(s):
            if j[x] == 1:
                return i
        return -1


# Valid Anagram

def isAnagram(self, s, t):
    # return sorted(s)==sorted(t)
    # return Counter(s) == Counter(t)
    s_count = Counter(s)
    for char in t:
        if char not in s_count:
            return False
        s_count[char] -= 1
        if s_count[char] == 0:
            del s_count[char]
    return len(s_count) == 0
