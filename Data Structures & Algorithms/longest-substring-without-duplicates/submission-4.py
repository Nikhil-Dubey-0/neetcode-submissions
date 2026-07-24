class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        left=0
        seen={}
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]]>=left:
                left=seen[s[i]]+1
                seen[s[i]]=i
                
            else:
                seen[s[i]]=i
                longest=max(longest,i-left+1)
        return longest