class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
      
# Runtime: 28 ms, faster than 81.90% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 14.1 MB, less than 67.77% of Python3 online submissions for Defanging an IP Address.
    
