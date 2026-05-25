class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        if not prices:
            return 0
        min_price = prices[0]
        for i in range(len(prices)):
            min_price= min(min_price,prices[i])
            profit=prices[i]-min_price
            if profit>maxi:
                maxi=profit
        return maxi

