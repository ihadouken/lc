# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: DFS + Recursion, Complexity: O(n), O(n)
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Equivalent trees have nulls at the same places (after potential flips).
        if not root1 and not root2:
            return True

        # Trees are not equivalent when there is a null but a corresponding valid
        # node in other tree or when trees have corresponding valid unequal nodes.
        if bool(root1) ^ bool(root2) or root1.val != root2.val:
            return False

        # Try checking for equivalence without flips. If that doesn't work check
        # after flipping left and right childs of second tree. If equivalence
        # still can't be established, trees are not flip equivalent.
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
            or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))
