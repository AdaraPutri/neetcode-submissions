class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(sorted(s)) != len(sorted(t)):
            return False
        return sorted(s) == sorted(t)
        