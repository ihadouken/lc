# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: BFS, Complexity: O(n), O(n)
# Tip: Incomplete trees have non-trailing null references in level traversal.

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        traversal = []

        while q:
            frontnode = q.popleft()
            if not frontnode:
                traversal.append(frontnode)
                continue

            traversal.append(frontnode.val)
            q.append(frontnode.left)
            q.append(frontnode.right)

        # Remove trailing null references.
        while not traversal[-1]:
            traversal.pop()

        # Any null references found now signify incompleteness.
        for val in traversal:
            if not val:
                return False
        return True

