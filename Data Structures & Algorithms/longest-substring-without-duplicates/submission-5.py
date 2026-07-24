class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        current=0
        seen={}
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]]>=i-current:
                current=i-seen[s[i]]
                seen[s[i]]=i
            else:
                seen[s[i]]=i
                current+=1
                longest=max(longest,current)
        return longest