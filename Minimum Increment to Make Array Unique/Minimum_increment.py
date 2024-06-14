class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                incr = nums[i - 1] - nums[i] + 1
                res += incr
                nums[i] += incr
        return res
