class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        min_price = prices[0]
        for price in prices[1:]:
            maximum = max(maximum, price - min_price)
            min_price = min(price, min_price)
        
        return maximum