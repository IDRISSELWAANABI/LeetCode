class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            m = left + (right - left) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                right = m - 1
            else:
                left = m + 1
        
        return -1
