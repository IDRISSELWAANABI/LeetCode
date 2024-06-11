class Solution:
    def longestPalindrome(self, s: str) -> int:
            counts = Counter(s)
            length = 0
            odd_present = False

            for count in counts.values():
                if count % 2 == 0:
                    length += count
                else:
                    length += count - 1
                    odd_present = True

            if odd_present:
                length += 1

            return length