class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        j=0
        t=True
        while j < len(min(strs, key=len)):
            for i in range(1,len(strs)):
                if strs[i][j]!=strs[0][j]:
                    t=False
            if t==True:
                res+=strs[0][j]
            j+=1
        return res

