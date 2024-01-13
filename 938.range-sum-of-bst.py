# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: DFS + Recursion, Complexity: O(n), O(h)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Null node contributes nothing to sum.
        if not root:
            return 0

        # If a node is too low, its left subtree has all low and invalid nodes.
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # If a node is too high, its right subtree has all high and invalid nodes.
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)

        # If node lies in valid range, add it to sum and process both subtrees.
        else:
            return (root.val
                + self.rangeSumBST(root.left, low, high)
                + self.rangeSumBST(root.right, low, high)
            )
