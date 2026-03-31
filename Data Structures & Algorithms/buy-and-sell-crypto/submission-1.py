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


# ⏱ Time Complexity: O(n)
# You loop through the prices one time from left to right.
# Each day you only do constant-time work:
# update min price
# calculate today’s profit
# update max profit
# No nested loops, no re-scanning.
# So total work grows only with the number of days → O(n).

# 🧠 Space Complexity: O(1)
# You only store two numbers:
# min_price_so_far
# max_profit
# These stay the same size no matter how big the input is.
# So memory usage is constant → O(1).