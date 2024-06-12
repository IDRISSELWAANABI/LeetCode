class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        for j in range(n):
            for i in range(n-1): 
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1], nums[i]
