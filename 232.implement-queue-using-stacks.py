# Approach: Stack (Two)
# Tip: Keep track of a LIFO and a (derived) FIFO ordering.

class MyQueue:
    # Complexity: O(1)
    def __init__(self):
        # Use another stack to convert LIFO order of original stack to FIFO.
        self.stack = []
        self.aux_stack = []

    # Complexity: O(1)
    def push(self, x: int) -> None:
        self.stack.append(x)

    # Complexity: O(n)
    # Helper to move all elements to aux_stack i.e. LIFO -> FIFO.
    def move2aux(self) -> None:
        while self.stack:
            self.aux_stack.append(self.stack.pop())

    # Complexity: O(1) (amortized)
    def pop(self) -> int:
        # If no more elements are remaining in FIFO order, convert current LIFO
        # ordering to FIFO.
        if not self.aux_stack:
            self.move2aux()
        # If FIFO ordering exists, its topmost element is the oldest.
        return self.aux_stack.pop()

    # Complexity: O(1) (amortized)
    def peek(self) -> int:
        if not self.aux_stack:
            self.move2aux()
        return self.aux_stack[-1]

    # Complexity: O(1)
    def empty(self) -> bool:
        # Queue is empty when both FIFO and LIFO orderings are empty.
        return len(self.stack) == 0 and len(self.aux_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
