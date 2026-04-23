class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_min = float('inf')
        for val in prices:
            if val < curr_min:
                curr_min = val
            elif val - curr_min > max_profit:
                max_profit = val - curr_min
        return max_profit