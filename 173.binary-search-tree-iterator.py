# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: DFS + Stack
class BSTIterator:
    # Complexity: O(1)
    def __init__(self, root: Optional[TreeNode]):
        # Use stack to store nodes to be processed later.
        self.stack = []
        self.cur = root

    # Complexity: O(1)
    def next(self) -> int:
        # Continue moving left (saving current node in stack) until not possible.
        # Left subtrees are processed first according to Left-Root-Right order.
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

        # Retrive a saved node if last node had no left or no right.
        if not self.cur:
            self.cur = self.stack.pop()

        # Update current pointer to explore the right subtree in later next()
        # calls after processing current node as per Left-Root-Right order. Save
        # value of current node before updating pointer.
        curval = self.cur.val
        self.cur = self.cur.right
        return curval

    # Complexity: O(1)
    def hasNext(self) -> bool:
        # No further traversal if there is no node stored in current pointer and
        # no saved unprocessed nodes exist.
        return self.stack or self.cur


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
