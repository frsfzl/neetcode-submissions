class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        longest = 0
        left = 0
        for right in range(len(s)):
            while s[right] in count:
                count.remove(s[left])
                left += 1
            count.add(s[right])
            longest = max(len(count), longest)

        return longest                