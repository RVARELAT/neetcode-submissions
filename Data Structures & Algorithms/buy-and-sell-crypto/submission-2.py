class Solution:
    def maxProfit(self, prices: List[int]) -> int:    
        left = 0 # left is buy 
        right = 1 # right is selling 
        max_profit = 0
        
        while right < len(prices):
            # is this a profitable transaction?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            # not a profitable transaction
            else:
                # we make left the right pointer since we found a low price
                left = right
                
            right += 1

        return max_profit
