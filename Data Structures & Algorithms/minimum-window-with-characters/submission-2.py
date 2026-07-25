from collections import Counter
class Solution:
    def window_valid(self):
        for x in self.coun.keys():
            if self.coun[x] > self.freq.get(x,0):
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        self.freq={}
        left = 0
        self.coun = Counter(t)
        shortest = len(s)
        values=(-1,-1)
        if len(s)<len(t):
            return ""
        for i in range(len(s)):
            self.freq[s[i]]=self.freq.get(s[i],0) + 1
            
            while self.window_valid():
                shortest = min(shortest,i-left)
                if shortest == i-left:
                    values = (left,i)
                self.freq[s[left]] -=  1
                left +=1 
                



        return s[values[0]:values[1]+1]
