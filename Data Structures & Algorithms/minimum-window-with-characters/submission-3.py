from collections import Counter

class Solution:
    def window_valid(self):
        for ch in self.coun:
            if self.freq.get(ch, 0) < self.coun[ch]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        self.freq = {}
        self.coun = Counter(t)

        left = 0
        shortest = float("inf")
        values = (-1, -1)

        for i in range(len(s)):
            self.freq[s[i]] = self.freq.get(s[i], 0) + 1

            while self.window_valid():
                if i - left + 1 < shortest:
                    shortest = i - left + 1
                    values = (left, i)

                self.freq[s[left]] -= 1
                left += 1

        if values == (-1, -1):
            return ""

        return s[values[0]:values[1] + 1]