from queue import Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: DFS, Complexity: O(n), O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Empty traversal for empty tree.
        if not root:
            return []

        # Use queue for storing the nodes layerwise along with their depth.
        bfs = Queue()
        # Add root to queue to initiate BFS with starting depth 0.
        bfs.put([root, 0])
        traversal = []

        # Traverse until tree is exhausted.
        while not bfs.empty():
            # Retrieve a node with its depth from queue.
            cur, depth = bfs.get()

            # Push the children of retrieved node for traversing next level.
            if cur.left:
                bfs.put([cur.left, depth+1])
            if cur.right:
                bfs.put([cur.right, depth+1])

            # If node is first node in the level, add to a separate sublist.
            if len(traversal) == depth:
                traversal.append([cur.val])
            # Else add to the sublist corresponding to its depth.
            else:
                traversal[depth].append(cur.val)

        # Return matrix with each row = level in BT.
        return traversal
