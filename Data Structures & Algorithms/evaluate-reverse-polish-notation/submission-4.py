class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            match ch:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                case "/":
                    a = stack.pop()
                    b = stack.pop()
                    # stack.append(stack[a] // stack[b])
                    # try:
                    stack.append(int(b / a))
                    # except:

                case "*":
                    stack.append(stack.pop() * stack.pop())
                case _:
                    stack.append(int(ch))
        return stack[0]