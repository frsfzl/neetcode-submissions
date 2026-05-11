class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counter = {}
        l, r = 0, 0
        
        while r < len(s):
            counter[s[r]] = counter.get(s[r], 0) + 1
            
            while r - l + 1 - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1

        return longest

