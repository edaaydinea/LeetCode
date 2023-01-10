class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
            return
        if val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # Push top of min stack again
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if len(self.stack) > 0:
            # Much simple than solution 1
            # But use more space
            self.min_stack.pop()
            self.stack.pop()

    def top(self) -> None:
        if len(self.stack) > 0:
            return self.stack[-1]
        return None

    def getMin(self) -> None:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
