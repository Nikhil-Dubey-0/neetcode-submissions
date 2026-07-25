from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count=Counter(s1)
        freq={}
        l=len(s1)
        if len(s2)<l:
            return False
        for i in range(len(s2)):
            freq[s2[i]]= freq.get(s2[i],0) + 1
            if i>=l:
                freq[s2[i-l]] -= 1
                if freq[s2[i-l]] == 0:
                    del freq[s2[i-l]]
                # freq[s2[i-l]]= freq.get(s2[i-l]) - 1
            if freq==s1_count:
                return True
        return False