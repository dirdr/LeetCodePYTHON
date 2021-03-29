class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # standard BS
        start, end = 0, len(nums) - 1
        while (start <= end):
            mid = start + (end - start) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
      
# Runtime: 244 ms, faster than 29.01% of Python3 online submissions for Binary Search.
# Memory Usage: 15.5 MB, less than 68.43% of Python3 online submissions for Binary Search.
            
            

        
