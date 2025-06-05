# Theodore Reyes
#
# Explanation: This solution records the amounts of profit
# that could potentially be dervied during each interval of
# the stocks growth, and returns the largest value found
# from these amounts as output

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        highest = prices[0]
        profit = 0
        maxProfit = 0
        for price in prices:
            if price > highest:
                highest = price
                profit = highest - lowest
                if (profit > maxProfit): maxProfit = profit
                continue
            if price < lowest:
                lowest = price
                highest = price
                continue
        return maxProfit
