class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix = ""
        i = 1 
        while not self.isPalindrome(prefix+s):
            prefix += s[-i]
            i+=1
        return prefix + s
    def isPalindrome(self, s):
        return s == s[::-1]