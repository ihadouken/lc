# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: DFS (Postorder) + Recursion, Complexity: O(n), O(h)
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # Initialize max univalue path length to minimum i.e. zero.
        cur_max = 0

        # Find max univalue path length involving given node and at most one of
        # its subtrees.
        def dfs(cur: Optional[TreeNode]) -> int:
            # Base Case: Null Node.
            if not cur:
                return -1

            # Save path lengths using node's children.
            leftval = dfs(cur.left)
            rightval = dfs(cur.right)

            # Initialize confirmed univalue path lenght from both children to -1.
            left_len, right_len = -1, -1

            # Path extension from either child can occur only if it has value
            # equal to current node. Store confirmed univalue paths lengths
            # extensible to current node in separate vars.
            if cur.left and cur.val == cur.left.val:
                left_len = leftval
            if cur.right and cur.val == cur.right.val:
                right_len = rightval

            # Declare "cur_max" as "nonlocal" for persistence outside call scope.
            nonlocal cur_max

            # Find max univalue path using:
            # 1) left subtree
            # 2) right subtree
            # 3) left and right subtree
            cur_max = max(cur_max, left_len+1, right_len+1, left_len+right_len+2)

            # Return max univalue path possible involving either left or right
            # subtree. Only one subtree must involved for binary tree paths
            # extending to ancestors.
            return max(left_len, right_len) + 1

        # Initiate DFS on root node.
        dfs(root)
        # Return global maximum length of univalue path in the tree.
        return cur_max
