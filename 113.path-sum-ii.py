# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: DFS + Recursion, Complexity: O(n), O(h)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Store all desired paths in "paths" and store node values of current
        # path in "curpath".
        paths = []
        curpath = []

        def dfs(cur: Optional[TreeNode], target: int):
            # Traverse current node by adding its value in "curpath".
            curpath.append(cur.val)
            # Decrease target requirement by value of current node.
            target -= cur.val

            # If a leaf is reached and target is met, record current path.
            if target == 0 and not cur.left and not cur.right:
                paths.append(curpath.copy())

            # Branch off to left and right subtrees of curren node to explore
            # further paths down it.
            if cur.left:
                dfs(cur.left, target)
            if cur.right:
                dfs(cur.right, target)

            # Remove current node to path after exploring all from paths it.
            # Backtrack and try other nodes at its position.
            curpath.pop()

        # No need to find paths in empty tree.
        if root:
            dfs(root, targetSum)
        # Return all accumated paths with node values summing up to target.
        return paths
