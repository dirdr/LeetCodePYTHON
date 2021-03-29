class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        self.nums, self.target = nums, target
        return self.binarySearch(0, len(nums) - 1)
        
    def binarySearch(self, start: int, end: int) -> int:
        if start > end:
            return -1
        mid = start + (end - start) // 2
        if self.nums[mid] == self.target:
            return mid
        else: 
            return self.binarySearch(mid + 1, end) if self.nums[mid] < self.target else self.binarySearch(start, mid - 1)
    
# Runtime: 224 ms, faster than 96.87% of Python3 online submissions for Binary Search.
# Memory Usage: 15.4 MB, less than 90.43% of Python3 online submissions for Binary Search.
            
