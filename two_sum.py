class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,num in enumerate(nums):
            lost = target-num
            if lost in map : 
               return[map[lost], i ]
            map[num]=i
        return[-1,-1]