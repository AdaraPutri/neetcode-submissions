# sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubstring, l = 0, 0
        uniqueSet = set()

        for r in range(len(s)):
            while s[r] in uniqueSet:
                uniqueSet.remove(s[l])
                l += 1
            uniqueSet.add(s[r])
            maxSubstring = max(maxSubstring, len(uniqueSet))

        return maxSubstring
        
        while l < len(s):
            if l == 0:
                r = l
                substring = s[l:r+1]
            else:
                r += 1
                substring = s[l:r]
            while r + 1 < len(s) and s[r+1] not in substring:
                r += 1
                substring = s[l:r+1]
            maxSubstring = max(maxSubstring, len(substring))
            l += 1

        return maxSubstring