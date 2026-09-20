class MinStack:
    # stack = [1,2,0]
    # getminstack = []
    def __init__(self):
        self.stack = []
        self.getminstack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.getminstack:
             self.getminstack.append(val)
        else:
            self.getminstack.append(min(val, self.getminstack[-1]))
        
        

            

        
        

    def pop(self) -> None:
        self.stack.pop()
        self.getminstack.pop()
        

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.getminstack[-1]
        
        
