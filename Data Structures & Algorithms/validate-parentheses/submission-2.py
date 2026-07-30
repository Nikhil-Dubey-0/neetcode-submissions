class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        cl = {"}":"{","]":"[",")":"("}
        op = {"{","[","("}
        for ch in s:
            if ch in op:
                stack.append(ch)
            elif stack and cl[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
