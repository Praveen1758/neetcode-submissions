class MinStack:

    def __init__(self):
        self.mainstack = []
        self.minstack = []
        
    def push(self, val: int) -> None:
        self.mainstack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif (val <= self.minstack[-1]):
            self.minstack.append(val)

    def pop(self) -> None:
        if self.mainstack[-1] == self.minstack[-1]:
            self.minstack.pop()

        self.mainstack.pop()

    def top(self) -> int:
        return self.mainstack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        