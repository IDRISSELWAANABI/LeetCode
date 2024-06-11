class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0,0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i]<=nums2[j]:
                res.append(nums1[i])
                i+=1
            elif nums1[i]>=nums2[j] :
                res.append(nums2[j])
                j+=1
        if i == len(nums1) and j<len(nums2):
            res.extend(nums2[j:len(nums2)])
        if j == len(nums2) and i<len(nums1):
            res.extend(nums1[i:len(nums1)])     


        if len(res)%2 != 0 :
            return res[len(res)//2]
        else : 
            return (res[(len(res)//2)-1]+res[(len(res)//2)])/2
        