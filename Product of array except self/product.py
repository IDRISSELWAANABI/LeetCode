class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1 
        postfix_product = 1 
        result = [0 for i in range(n)]
        for i in range (n):
            result[i]=prefix_product
            prefix_product *= nums[i]
        for j in range(n-1,-1,-1):
            result[j] *= postfix_product 
            postfix_product *= nums[j]
        return result 