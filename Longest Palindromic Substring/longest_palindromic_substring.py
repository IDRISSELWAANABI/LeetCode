class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)
        longest_palindrome = ""

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                    longest_palindrome = substring

        return longest_palindrome
