# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: DFS + Recursion + Backtracking, Complexity: O(n), O(h)
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # "paths" to store all root-to-leaf paths and "curpath" to store node
        # values in path being traversed.
        paths, curpath = [], []
        sep = '->'

        def dfs(cur: Optional[TreeNode]):
            # Store current node as it traversed now.
            curpath.append(cur.val)

            # Leaf node means ending of a path.
            if not cur.left and not cur.right:
                # Combine node values in path into path string i.e. "2->3->1" .
                pathstr = sep.join(map(str, curpath))
                # Store generated path's string to "paths" for returning later.
                paths.append(pathstr)

            # Branch to current node's left and right if they exits.
            if cur.left:
                dfs(cur.left)
            if cur.right:
                dfs(cur.right)

            # Remove added node after exploring paths extending down from it to
            # find other paths having other nodes in its place.
            curpath.pop()

        # Initiate DFS from root and populate "paths".
        dfs(root)
        # Return list of all root-to-leaf paths.
        return paths
