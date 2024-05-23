class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < target:
                l += 1
            elif nums[r] > target:
                r -= 1
            else:
                break
        if l > r:
            return [-1, -1]
        return [l, r]