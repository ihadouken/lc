# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: BFS, Complexity: O(n), O(n)
    # Tip: Reverse alternate rows after standard BFS.
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0))
        levels = []

        while q:
            node, depth = q.popleft()
            if not node:
                continue

            q.append((node.left, depth+1))
            q.append((node.right, depth+1))

            if len(levels) == depth:
                levels.append([node.val])
            else:
                levels[depth].append(node.val)

        dir = 1
        for level in levels[1::2]:
            level.reverse()

        return levels
