class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        splited = s.split()
        result = ""
        for i in range (k):
            result += splited[i]
            if i != k-1:
                result += " "
        return result
      
      
# Runtime: 16 ms, faster than 100.00% of Python3 online submissions for Truncate Sentence.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Truncate Sentence.      
