class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = []
        for ch in s.lower():
            if ch.isalnum():
                s2.append(ch)
        l, r = 0, len(s2) - 1 
        while l < r:
            if s2[l] is not s2[r]:
                return False
            l += 1
            r -= 1
        
        return True