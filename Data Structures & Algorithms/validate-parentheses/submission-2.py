class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"}": "{", ")": "(", "]": "["}
        for c in s:
            if stack and c in pairs:
                if stack[-1] != pairs[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return not stack