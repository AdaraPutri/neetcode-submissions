# goal: to maximize the number of same letters in the string
# start from left, count frequency of each letter in substring
# c = subtract length of substring with highest frequency
# keep maxSub variable with max() function
# while c is less than or equal to k, move right pointer to right
# else move left pointer to the right (use for loop)
# no actual letter conversion needs to take place

# hashset, key: A, value: frequency (defaultdict(int))

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxSub, c, r = 0, 0, 0
        l = 0
        freq[s[l]] += 1
        while r < len(s) - 1:
            r += 1
            freq[s[r]] += 1
            c = (r - l + 1) - max(freq.values())
            while c > k:
                freq[s[l]] -= 1
                l += 1
                c = (r - l + 1) - max(freq.values())
            maxSub = max(maxSub, r - l + 1)

        return maxSub



        

