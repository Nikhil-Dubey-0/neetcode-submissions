class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        for x in range(1,len(prices)):
            for i in range(x,len(prices)):
                diff=prices[i]-prices[i-x]
                maxi = max(maxi,diff)
        return maxi
