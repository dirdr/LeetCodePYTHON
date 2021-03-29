# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        start = 1
        end = n
        
        while (True):
            
            mid = (start + end)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                start = mid + 1
            else:
                end = mid - 1
 
# Runtime: 28 ms, faster than 79.86% of Python3 online submissions for Guess Number Higher or Lower.
# Memory Usage: 14.3 MB, less than 45.53% of Python3 online submissions for Guess Number Higher or Lower.

                
                
