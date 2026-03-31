class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # add val to our regular func. that keeps track of order
        self.stack.append(val)

        if self.minStack != []:
            val = min(val, self.minStack[-1])
            self.minStack.append(val)
        else:
            # the current val would be the min
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        # min stack still has the min before this number was added
        self.minStack.pop()

    def top(self) -> int:
        # only clled when stack is empty so don't need to worry about edge cased
        return self.stack[-1]

    def getMin(self) -> int:
        # # only clled when stack is empty so don't need to worry about edge cased
        return self.minStack[-1]

        
