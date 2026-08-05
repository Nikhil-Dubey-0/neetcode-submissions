class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr, out = prices[0],0
        for i in prices[1:]:
            if i >= curr:
                out += i - curr

            curr = i
        return out