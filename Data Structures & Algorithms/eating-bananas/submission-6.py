class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                min_k = min(k, min_k)
                r = k - 1
            else:
                l = k + 1
        
        return min_k