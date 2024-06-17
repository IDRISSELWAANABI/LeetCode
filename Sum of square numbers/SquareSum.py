class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for prime in range(2, int(math.sqrt(c)) + 1):
            if c % prime == 0:
                count = 0
                while c % prime == 0:
                    c //= prime
                    count += 1
                if prime % 4 == 3 and count % 2 != 0:
                    return False
        return c % 4 != 3

        