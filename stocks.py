class Solution:
    def maxProfit(self, prices: list[int]) -> tuple[int, int, int]:
        l, r = 0, 1          # Left (buy), Right (sell) pointers
        max_profit = 0        # Maximum profit
        buy_day, sell_day = 0, 0  # Track best buy and sell days
        
        while r < len(prices):
            if prices[l] < prices[r]:
                current_profit = prices[r] - prices[l]
                if current_profit > max_profit:
                    max_profit = current_profit
                    buy_day, sell_day = l, r
            else:
                l = r  # Move buy day to current position (cheaper price)
            r += 1     # Always move sell day forward
            
        return max_profit, buy_day, sell_day