class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1, 2]
        for i in range(2, n + 2):
            res.append(res[i - 1] + res[i - 2])

        return res[n-1]
