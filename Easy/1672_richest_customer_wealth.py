class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for customerAccount in accounts:
            tempMax = 0
            for amount in customerAccount:
                tempMax += amount
            if tempMax > max:
                max = tempMax
        return max
                
# Runtime: 52 ms, faster than 77.74% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 14.1 MB, less than 95.63% of Python3 online submissions for Richest Customer Wealth.
        
