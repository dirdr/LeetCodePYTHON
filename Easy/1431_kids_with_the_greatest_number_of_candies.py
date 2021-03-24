class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandiesValue = max(candies)
        return  [candy + extraCandies >= maxCandiesValue for candy in candies]
     
# Runtime: 40 ms, faster than 57.65% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 14.2 MB, less than 82.37% of Python3 online submissions for Kids With the Greatest Number of Candies.
        
        
