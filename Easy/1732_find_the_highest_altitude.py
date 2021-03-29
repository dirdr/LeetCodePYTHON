class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentAlt = 0
        max = 0
        for i in range(len(gain)):
            currentAlt += gain[i]
            if currentAlt > max:
                max = currentAlt
        return max
      
# Runtime: 36 ms, faster than 59.30% of Python3 online submissions for Find the Highest Altitude.
# Memory Usage: 14.2 MB, less than 71.51% of Python3 online submissions for Find the Highest Altitude.


        
