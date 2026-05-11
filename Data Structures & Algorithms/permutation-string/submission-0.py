class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for char in s1:
            count[char] = count.get(char, 0) + 1

        l = 0
        for r in range(len(s2)):
            if s2[r] in count:
                count[s2[r]] -= 1
            
            if max(count.values()) == 0:
                return True

            if r - l + 1 == len(s1):
                if s2[l] in count:
                    count[s2[l]] += 1
                l += 1
        return False
