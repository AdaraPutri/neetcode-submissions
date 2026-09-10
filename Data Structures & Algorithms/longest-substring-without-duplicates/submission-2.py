# sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubstring, l = 0, 0
        
        while l < len(s):
            r = l
            substring = s[l:r+1]
            while r + 1 < len(s) and s[r+1] not in substring:
                r += 1
                substring = s[l:r+1]
            maxSubstring = max(maxSubstring, len(substring))
            l += 1

        return maxSubstring

# xyzzzx
