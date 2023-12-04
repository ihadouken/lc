# Each entry in history can access one entry before it and after it.
class Node:
    def __init__(self, val="", prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# Approach: Doubly Linked List
class BrowserHistory:

    # Complexity: O(1)
    # Initialize the history's linked list with the homepage.
    def __init__(self, homepage: str):
        self.cur = self.tail = Node(homepage)

    # Complexity: O(1)
    # Create a new history node for visited page and insert it just after the
    # current node. Nodes after current are autoremoved by garbage collector.
    # Visited node (being the most recent) is set the current and also the last
    # node in history.
    def visit(self, url: str) -> None:
        visited = Node(url)
        visited.prev = self.cur

        self.cur.next = visited
        self.cur = self.tail = visited

    # Complexity: O(steps), O(1)
    # Move back in the history "steps" times or until first entry is reached.
    def back(self, steps: int) -> str:
        while steps and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    # Complexity: O(steps), O(1)
    # Move forward in the history "steps" times or until last entry is reached.
    def forward(self, steps: int) -> str:
        while steps and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
