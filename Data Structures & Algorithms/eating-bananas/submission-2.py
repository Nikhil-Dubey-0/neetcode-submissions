class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = 1
        maxi = max(piles)
        out = maxi
        while mini<=maxi:
            mid = (mini+maxi) // 2
            hours = 0
            for pile in piles:
                hours += pile//mid 
                if pile%mid != 0:
                    hours+=1
            if hours > h:
                mini = mid+1
            else:
                out = mid
                maxi = mid-1
        return out
    