# Approach: Stack + Lazy Evaluation, Complexity: O(1) for all operations.
class CustomStack:
    def __init__(self, maxSize: int):
        # Use dynamic arrays to store stack of values and stack of increments.
        self.incr, self.stack = [], []
        self.capacity = maxSize

    def push(self, x: int) -> None:
        # Add a new element (with default increment 0) if possible.
        if len(self.stack) < self.capacity:
            self.stack.append(x)
            self.incr.append(0)

    def pop(self) -> int:
        # Return -1 for empty stack.
        if not self.stack:
            return -1

        # Since elements were incremented starting from bottom, increment of an
        # element must be saved into the increment of its predecessor before it
        # is popped.
        if len(self.incr) > 1:
            self.incr[-2] += self.incr[-1]

        # Remove the topmost value along with its increment and return their sum.
        return self.stack.pop() + self.incr.pop()

    def increment(self, k: int, val: int) -> None:
        # Don't increment on empty stack.
        if self.stack:
            # If k > number of elements in stack, increment all present values.
            i = min(len(self.incr), k) - 1
            # incr[i] denotes an increment for all indices in range [0, i].
            self.incr[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
