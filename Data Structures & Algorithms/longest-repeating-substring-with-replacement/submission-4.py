class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right,long=0,0,0
        freq={}
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            if right-left+1-max(freq.values())<=k:
                right+=1
            else:
                freq[s[left]]-=1
                freq[s[right]]-=1
                left+=1
            long = max(long,right-left)
        return long