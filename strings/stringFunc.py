# Reverse String

from typing import List


class Solution:
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
