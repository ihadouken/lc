# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # # Approach: DFS + Stack, Complexity: O(n), O(h)
    # # Tip: If inorder traversal visits nodes in sorted order, the tree is a BST.
    #
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     cur = root
    #     stack, nums = [], []
    #
    #     # Traversal stops after bottom-right node.
    #     while cur or stack:
    #         # Keep going left until there is no left. Add skipped nodes to stack.
    #         while cur:
    #             stack.append(cur)
    #             cur = cur.left
    #
    #         # Backtrack to last valid node using stack.
    #         if stack:
    #             cur = stack.pop()
    #         # Visit the node and move to its right to process its right subtree.
    #         nums.append(cur.val)
    #         cur = cur.right
    #
    #     # Check if the inorder traversal produced a sorted list.
    #     for i in range(len(nums)-1):
    #         if nums[i] >= nums[i+1]:
    #             return False
    #     return True
    #
    # # Approach: DFS + Recursion, Complexity: O(n), O(h)
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     nums = []
    #
    #     def dfs(cur: Optional[TreeNode]) -> None:
    #         if not cur:
    #             return
    #
    #         dfs(cur.left)
    #         nums.append(cur.val)
    #         dfs(cur.right)
    #
    #     dfs(root)
    #     for i in range(len(nums)-1):
    #         if nums[i] >= nums[i+1]:
    #             return False
    #     return True

    # Approach: DFS + Recursion, Complexity: O(n), O(h)
    # Tip: Every node in BST has a range associated with it which decides its
    #      validity. Root's value (say x) lies in (-∞, ∞). Every node in
    #      its left subtree must lie in (-∞, x) and every node in its right
    #      subtree lies in (x, ∞). This rule is recursively true for all nodes.

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur: Optional[TreeNode], beg: int, end: int) -> bool:
            if not cur:
                return True
            return beg < cur.val < end and dfs(cur.left, beg, cur.val) and dfs(cur.right, cur.val, end)

        return dfs(root, float('-inf'), float('inf'))
