# Approach: Stack, Complexity: O(1) for all operations, O(n) for extra stack.
class MinStack:
    def __init__(self):
        # Maintain a min for every value added in stack. Build a stack with
        # minimum values corresponding to every value.
        self.vals = []
        self.mins = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        if self.mins:
            # If val < last minimum, val is the minimum corresponding to itself.
            # Else, repeat the last minimum as the minimum again.
            self.mins.append(min(val, self.mins[-1]))
        else:
            self.mins.append(val)

    # Pop from both stacks i.e. remove element along with its minimum.
    def pop(self) -> None:
        if self.vals:
            self.vals.pop()
            self.mins.pop()

    # Return the top of stack containing values.
    def top(self) -> int:
        if not self.vals:
            return None
        return self.vals[-1]

    # Top of "stack of mins" is the global minima of "stack of values".
    def getMin(self) -> int:
        if not self.vals:
            return None
        return self.mins[-1]


# Your self.minstack object will be instantiated and called as such:
# obj = self.minstack()
# obj.push(val)
# obj.pop()
# param_3 = obj.-1()
# param_4 = obj.getMin()
