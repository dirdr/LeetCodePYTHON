class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tempResult = 0
        result = []
        for num in nums:
            tempResult += num
            result.append(tempResult)
        return result

# Runtime: 40 ms, faster than 68.02% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.4 MB, less than 74.14% of Python3 online submissions for Running Sum of 1d Array.
     
