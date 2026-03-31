class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # start at first two indices
        smallest_price_so_far = float('inf')
        best_profit = 0
        
        for price in prices:
            # 3a: update max_profit based on selling today
            if price - smallest_price_so_far > best_profit:
                best_profit = price - smallest_price_so_far
            # 3b: update min_price based on today's price
            if price < smallest_price_so_far:
                smallest_price_so_far = price
        
        return best_profit