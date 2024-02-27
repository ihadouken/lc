# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: DFS (Postorder) + Recursion, Complexity: O(n), O(h)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize maximum path sum with minimum possible value.
        max_sum = float('-inf')

        # Find sum of maximum path starting from given node and involving at most
        # one of its subtrees.
        def find_max_sub(cur: Optional[TreeNode]) -> int:
            # If there are no nodes, the sum is 0.
            if not cur:
                return 0

            # Find maximum path sum for each subtree.
            left_max = find_max_sub(cur.left)
            right_max = find_max_sub(cur.right)

            # Python construct to access primitives in outer function's scope.
            nonlocal max_sum

            # Find sum of max path starting from current node using:
            # 1) None of the subtrees.
            # 2) Left subtree.
            # 3) Right subtree.
            # 4) Both subtrees.
            cur_max = max(cur.val, cur.val+left_max, cur.val+right_max, cur.val+left_max+right_max)
            # Update global max.
            max_sum = max(max_sum, cur_max)

            # Return max path sum from current node using at most one subtree. At
            # most one subtree must be used as the path may be extended upward to
            # one of current node's ancestors.
            return max(cur.val, cur.val+left_max, cur.val+right_max)

        # Initiate the recursive DFS routine on root.
        find_max_sub(root)
        # Return global max path sum.
        return max_sum
