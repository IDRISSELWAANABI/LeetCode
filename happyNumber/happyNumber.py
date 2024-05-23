class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_digits(m): 
            r = 0
            for i in str(m):
                r += int(i)**2
            return r 

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_of_digits(n)
        return n == 1