class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        left, right = 1, max(piles)
        res = right
        while left <= right:
            k = (left + right) // 2
            hours = 0
            for num in piles:
                hours += math.ceil(num / k)
            if hours > h:
                left = k + 1
            else:
                right = k - 1
                res = min(k, res)

        return res