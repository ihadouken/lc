# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: DFS + Recursion, Complexity: O(n), O(n)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Use dict to hold variable global to inner (recursive) function.
        globals = {}
        # Global var to store sum of all nums in tree.
        globals['sum'] = 0

        # Each tree path produces a number. DFS to traverse each path.
        def add_digit(cur: Optional[TreeNode], num: int):
            # N * 10 shifts each digit in number N to left by 1 then add the new
            # digit (cur.val) as new LSB of N.
            num = num * 10 + cur.val

            # Leaf node adds the last digit to a number.
            if not cur.left and not cur.right:
                # Increment sum by generated number.
                globals['sum'] += num

            # If non-leaf node has left subtree, process paths down it.
            if cur.left:
                add_digit(cur.left, num)
            # If non-leaf node has right subtree, process paths down it.
            if cur.right:
                add_digit(cur.right, num)

        # Initiate DFS at root and give it an initial number 0.
        add_digit(root, 0)
        # Return the sum of all numbers in tree paths.
        return globals['sum']
