class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_freq = 0
        longest = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Highest frequency of any character seen in the current window
            max_freq = max(max_freq, freq[s[right]])
# Notice that we never decrease max_freq.
# "If the most frequent character leaves the window, shouldn't max_freq decrease?"
# No. We intentionally leave it as is.
# It may become stale (slightly larger than the true maximum frequency in the current window),
# but the algorithm is still correct and remains O(n).


            # If more than k replacements are needed, shrink the window
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update the answer
            longest = max(longest, right - left + 1)

        return longest