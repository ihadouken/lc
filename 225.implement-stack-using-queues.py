# Approach: Queue (One)
class MyStack:
    def __init__(self):
        # Single queue used to implement stack.
        self.queue = collections.deque()

    # Complexity: O(1)
    def push(self, x: int) -> None:
        # Insert new items at the back of the queue.
        self.queue.append(x)

    # Complexity: O(n)
    def pop(self) -> int:
        # For all but last item, Remove (from front) and reinsert (at back). This
        # ends up rotating the entire queue clockwise except the one element at
        # back moved from back now to front. Now, it can easily be removed.
        N = len(self.queue)
        for _ in range(N-1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    # Complexity: O(n)
    def top(self) -> int:
        # Similar to popping the top (back), accessing the top (back) requires
        # removing and reinserting all elements except top (back). After this,
        # top moves from back to front of queue.
        N = len(self.queue)
        for _ in range(N-1):
            self.queue.append(self.queue.popleft())

        # Peek it from the front. Restore the top to previous position i.e. back
        # after accessing by removing and reinserting it.
        top = self.queue.popleft()
        self.queue.append(top)
        return top

    # Complexity: O(1)
    def empty(self) -> bool:
        return len(self.queue) == 0


# your mystack object will be instantiated and called as such:
# obj  myStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
