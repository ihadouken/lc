# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: DFS + Stack, Complexity: O(n), O(n)
# Tip: Store nodes in a stack as a path is traversed. Max path in the tree = Max size 
#      of stack during traversal of tree.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0
        stack, top = [], -1
        stack.append([root, 0])

        while stack:
            # Every stack entry holds a node and its state. State determine if
            # its children are visited yet.
            topnode, state = stack[top]

            # Handle empty tree and nulls added due to absense of node.
            if not topnode:
                stack.pop()
                continue

            # Stack size increases as a path is traversed.
            maxdepth = max(maxdepth, len(stack))

            if state == 0:
                stack[top][1] += 1
                stack.append([topnode.left, 0])
            elif state == 1:
                stack[top][1] += 1
                stack.append([topnode.right, 0])
            else:
                stack.pop()

        return maxdepth
