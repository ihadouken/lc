# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: BFS, Complexity: O(m+n), O(m+n)
    # Tip: There a one-one relation between a tree and a level order traversal.

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root: Optional[TreeNode]) -> List[int|str]:
            traversal = []
            q = deque()
            q.append(root)

            while q:
                node = q.popleft()
                if not node:
                    traversal.append('-')
                    continue

                traversal.append(node.val)
                q.append(node.left)
                q.append(node.right)

            return traversal

        return bfs(p) == bfs(q)
