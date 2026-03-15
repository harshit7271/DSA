from collections import Counter, defaultdict
import heapq

# Merge intervals
"""[[1,3],[2,6],[8,10],[15,18]"""


def merge(self, intervals):
    if intervals == []:
        return []
    result = []
    intervals.sort()
    for interval in intervals:
        if result == [] or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result


# Sort colors
"""[2,0,2,1,1,0]"""


class Solution(object):

    def sortColors(self, nums):
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] <= nums[i]:
                    nums[i], nums[j]= nums[j], nums[i]
        return nums           
        """

        red = 0
        white = 0
        blue = len(nums) - 1

        while white <= blue:
            curr = nums[white]
            if curr == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif curr == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        return nums


# Minimum number of coins  [Greedy algo]

# coins = [1,2,5,10,20,50,100, 200,500,2000]

def coinNum(self, coins, amount):
    result = []
    N = amount
    n = len(coins)
    for i in range(n-1, -1, -1):
        while N >= coins[i]:
            result.append(coins[i])
            N -= coins[i]
    return result

# Top K frequent elements


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        d = defaultdict(int)
        # will count the number of occurance of every elements
        for num in nums:
            d[num] += 1
        heap = []  
        for key, val in d.items(): 
            if len(heap) < k or val > heap[0][0]: 
                heapq.heappush(heap, [val, key])
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
        """
        d = Counter(nums)
        heap = []
        for num, freq in d.items():
            heapq.heappush(heap, (-freq, num))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


# fibonacci numbers

def fib(self, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    """
    else:
        return self.fib(n-1) + self.fib(n-2)"""
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b


# remove duplicates
def reemoveDuplicates(self, nums):
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right-1]:
            nums[left] = nums[right]
            left += 1
    return left


# Find all numbers disappeared in an array
def findMissingNumbers(self, nums):
    missing = []

    for i in nums:
        pos = abs(i) - 1
        if nums[pos] > 0:
            nums[pos] *= -1
    for i in range(len(nums)):
        if nums[i] > 0:
            missing.append(i+1)
    return missing


# find  the third last distict numbers

def thirdMax(sel, nums):

    nums = list(set(nums))  # get rid of duplicates
    nums.sort()
    if len(nums) <= 2:
        return nums[-1]
    return nums[-3]

    """
      nums = set(nums)
      if len(nums) < 3:
          return max(nums)
      nums.remove(max(nums))
      nums.remove(max(nums))
      return max(nums)
    """

# find pivot index


def pivotIndex(self, nums):
    left_sum = 0
    right_sum = sum[nums]  # type: ignore
    for i in range(len(nums)):
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1
