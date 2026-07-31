class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=None

    def push(self, val: int) -> None:
        # self.stack.append(val)
        if not self.stack:
            self.stack.append((val,None))
            self.mini = val
        else:
            self.stack.append((val,self.mini))
            self.mini= min(val,self.mini)
        

    def pop(self) -> None:
        if not self.stack:
            return
        self.mini=self.stack[-1][1]
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.mini

        
