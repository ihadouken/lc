# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: DFS + Stack, Complexity: O(n), O(n)
    # Note: This is a more elegant iterative DFS solution than the one below.

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Store nodes deferred for processing in stack.
        stack = []
        cur = root

        # Continue until no nodes (untraversed or deferred) are left.
        while cur or stack:
            # Keep going left deferring nodes on the way.
            while cur:
                stack.append(cur)
                cur = cur.left

            # When can't go further left, process a deferred node.
            cur = stack.pop()

            # Return value of kth node in the inorder traversal.
            k -= 1
            if not k:
                return cur.val

            # Do same process for the previously deferred node's right subtree.
            cur = cur.right


    # Approach: DFS + Stack, Complexity: O(n), O(n)
    # Tip: Inorder Traversal for BST is always sorted. Traverse till the kth node.

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     # Use stack to keep track of DFS.
    #     stack = []
    #     stack.append([root, False])
    #
    #     while stack:
    #         topnode, seen_left = stack[-1]
    #         # If a node has unexplored left subtree, DFS on its left child.
    #         if not seen_left and topnode.left:
    #             stack[-1][1] = True
    #             stack.append([topnode.left, False])
    #
    #         # Else process the node and then DFS on its right child.
    #         else:
    #             # Count k nodes by decrement k till its zero.
    #             k -= 1
    #             stack.pop()
    #
    #             # Return kth node's value.
    #             if k == 0:
    #                 return topnode.val
    #
    #             if topnode.right:
    #                 stack.append([topnode.right, False])
