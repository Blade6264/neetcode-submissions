class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if self.min_vals:
            self.min_vals.append(min(val, min(self.min_vals)))
        else:
            self.min_vals.append(val)
        
    def pop(self) -> None:
        self.min_stack.pop()
        self.min_vals.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]
        
