# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: DFS + Stack, Complexity: O(n), O(n)
# Tip: Inorder Traversal for BST is always sorted. Traverse till the kth node.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Use stack to keep track of DFS.
        stack = []
        stack.append([root, False])

        while stack:
            topnode, seen_left = stack[-1]
            # If a node has unexplored left subtree, DFS on its left child.
            if not seen_left and topnode.left:
                stack[-1][1] = True
                stack.append([topnode.left, False])

            # Else process the node and then DFS on its right child.
            else:
                # Count k nodes by decrement k till its zero.
                k -= 1
                stack.pop()

                # Return kth node's value.
                if k == 0:
                    return topnode.val

                if topnode.right:
                    stack.append([topnode.right, False])
