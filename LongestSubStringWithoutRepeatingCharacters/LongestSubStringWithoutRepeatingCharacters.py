class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return len(s)
        res = []
        length = 0 
        for i in range(len(s)):
            seen_chars = set()
            j = i
            while j < len(s) and s[j] not in seen_chars:
                seen_chars.add(s[j])
                length += 1
                j += 1
            res.append(length)
            length = 0
        return max(res)