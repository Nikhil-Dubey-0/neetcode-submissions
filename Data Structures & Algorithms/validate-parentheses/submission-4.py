class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for ch in s:
            if ch in pairs:
                stack.append(pairs[ch])   # Push expected closing bracket
            elif not stack or stack.pop() != ch:
                return False

        return not stack