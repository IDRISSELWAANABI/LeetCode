class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1       
        prefix_count = defaultdict(int)
        prefix_count[0] = 1          
        prefix_sum = 0
        result = 0        
        for num in nums:
            prefix_sum += num            
            if (prefix_sum - k) in prefix_count:
                result += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] += 1       
        return result