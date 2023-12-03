# Definition for a binary tree topnode.
# class Treetopnode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: DFS + Stack, Complexity: O(n), O(n)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Empty traversal for empty tree.
        if not root:
            return []

        # Use stack for DFS and initiate it by adding root to it.
        stack = []
        # Boolean determines if a node's children have been added to stack.
        stack.append([root, False])
        traversal = []

        while stack:
            topnode, seen = stack[-1]

            # If a node's children haven't been considered yet, add them to stack.
            if not seen:
                stack[-1][1] = True
                # Process right after left by adding it to stack before left.
                if topnode.right:
                    stack.append([topnode.right, False])
                if topnode.left:
                    stack.append([topnode.left, False])

            # If a node's children have been processed, it can be processed now.
            else:
                stack.pop()
                traversal.append(topnode.val)

        # Return list of nodes traversed in postorder fashion.
        return traversal
