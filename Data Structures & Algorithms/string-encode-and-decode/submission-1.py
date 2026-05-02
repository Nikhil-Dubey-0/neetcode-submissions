class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, encoded: str) -> List[str]:
        strs=[]
        i=0
        while i<len(encoded):
            j=i
            while encoded[j]!="#":
                j+=1
            lenth = int(encoded[i:j])

            strs.append(encoded[j+1:j+1+lenth])

            i=j+1+lenth

        return strs