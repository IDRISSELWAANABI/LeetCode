class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr1)
        m = len(arr2)
        res = []
        s = set()


        for i in range(m):
            for j in range(n):
                if arr1[j]==arr2[i]:
                    res.append(arr2[i])
                    s.add(arr2[i])
        res1 = []
        for i in arr1 : 
            if i not in s : 
                res1.append(i)

        res = res+sorted(res1)
                    

        return res 
            

        