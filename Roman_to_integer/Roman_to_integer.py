class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        p=0
        i=0
        L=['I','X','C']
        if s in dict : 
            return dict[s]
        else:
            while i < len(s)-1 : 
                if s[i] in L  and dict[s[i+1]]>dict[s[i]]:
                    p+=dict[s[i+1]]-dict[s[i]]
                    i+=2
                else : 
                    p+=dict[s[i]]
                    i+=1
            if s[-2]  in L and dict[s[-1]]>dict[s[-2]]:
                return p
            else:
                return p+dict[s[-1]]