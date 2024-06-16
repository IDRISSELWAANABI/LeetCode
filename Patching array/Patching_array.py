class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patched = 1
        result = 0
        i = 0
        while patched <= n:
            if i < len(nums) and nums[i] <= patched:
                patched += nums[i]
                i += 1
            else:
                patched += patched
                result += 1
        return result
