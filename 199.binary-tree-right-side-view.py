# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: BFS, Complexity: O(n), O(n)
    # Tip: The rightmost node in each level is the last one in that level.

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q, depth = deque(), 0
        q.append((root, depth))
        rights = []

        while q:
            node, depth = q.popleft()

            # A node is the last one a level if there are (currently) no other
            # nodes in the queue or all of them are at higher depth.
            if not q or depth != q[0][1]:
                rights.append(node.val)

            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))

        return rights
