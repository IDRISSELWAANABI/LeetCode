class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        temp = []
        for i in arr2 :  
            res.extend([i]*arr1.count(i))
        for i in arr1 :
            if  i not in arr2 : 
                temp.append(i)
        res.extend(sorted(temp))
        return res 
            

        