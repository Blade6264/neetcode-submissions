class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if self.min_vals:
            # this is is not O(1):
            # self.min_vals.append(min(val, min(self.min_vals)))
            # min(self.min_vals) is O(n)

            # to fix this, we know that the top of the min_vals stack
            # keeps track of the min value alr, so we can instead do
            # min(val, self.min_vals[-1]) as indexing the last elem is O(1)
            self.min_vals.append(min(val, self.min_vals[-1]))
        else:
            self.min_vals.append(val)
        
    def pop(self) -> None:
        self.min_stack.pop()
        self.min_vals.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]
        
