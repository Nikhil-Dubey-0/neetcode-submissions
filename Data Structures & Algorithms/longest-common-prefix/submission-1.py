class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com=""
        la = min([len(i) for i in strs])
        k=strs[0]
        for i in range(la):
            j=k[i:i+1]
            for s in strs:
                if s[i]!=j:
                    return com
            com+=j
        return com