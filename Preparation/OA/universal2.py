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
