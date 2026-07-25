class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        first= strs[0]
        last= strs[-1]
        j=0
        while(j<len(first)and j<len(last) and first[j]==last[j]):
           j+=1
        return first[:j]