# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Approach: DFS + Stack, Complexity: O(n), O(n)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Empty traversal for empty tree.
        if not root:
            return []

        stack = []
        stack.append(root)
        traversal = []

        while stack:
            # Add topmost node to traversed list before its children.
            topnode = stack.pop()
            traversal.append(topnode.val)

            # Visit right after left by putting it before left in stack.
            if topnode.right:
                stack.append(topnode.right)
            if topnode.left:
                stack.append(topnode.left)

        # Return list of traversed (in preorder fashion) nodes.
        return traversal
