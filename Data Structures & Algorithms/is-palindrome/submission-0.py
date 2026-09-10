# 1. read with a delimiter (' '), concatenate separate words in given sentence into one string
# 2. ''.join(str)
# 3. lower()
# 4. filter out non alphanumeric characters

class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = s.split(' ')
        words_joined = ''.join(words)
        words_joined = words_joined.lower()
        clean = ''

        for w in words_joined:
            if w.isalnum():
                clean += w

        idx_d = len(clean)

        for idx_u, up in enumerate(clean):
            idx_d = idx_d - 1
            down = clean[idx_d]

            if up != down:
                return False
                
            if idx_u >= idx_d:
                break

        return True