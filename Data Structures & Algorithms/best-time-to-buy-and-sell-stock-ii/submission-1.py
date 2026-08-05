class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev, out = prices[0],0
        for curr in prices[1:]:
            if curr > prev:
                out += curr - prev

            prev = curr
        return out