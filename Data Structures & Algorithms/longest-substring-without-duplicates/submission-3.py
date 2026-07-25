class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                maximum = max(maximum, len(seen))
            else:
                while s[right] in seen and left < right:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
        
        return maximum
