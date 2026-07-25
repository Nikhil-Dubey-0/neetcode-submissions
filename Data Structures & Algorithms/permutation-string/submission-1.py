from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count=Counter(s1)
        l=len(s1)
        if len(s2)<l:
            return False
        for i in range(len(s2)-l+1):
            if Counter(s2[i:i+l])==s1_count:
                return True
        return False