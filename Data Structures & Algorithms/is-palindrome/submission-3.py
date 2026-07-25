class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = []
        for char in s.lower():
            if char.isalnum():
                alpha.append(char)
        
        left, right = 0, len(alpha) - 1
        while left < right:
            if alpha[left] != alpha[right]:
                return False
            left += 1
            right -= 1
        
        return True