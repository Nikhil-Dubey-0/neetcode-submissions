from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        need = Counter(t)
        window = {}

        required = len(need)      # Number of distinct chars needed
        formed = 0                # Number of distinct chars currently satisfied

        left = 0
        best_len = float("inf")
        best_left = 0

        for right in range(len(s)):

            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # Just satisfied this character's requirement
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Window contains all required characters
            while formed == required:

                # Update answer
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                # Requirement is no longer satisfied
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_left:best_left + best_len]