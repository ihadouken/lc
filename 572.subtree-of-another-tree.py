# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from hashlib import sha256

class Solution:
    # Approach: Hashing (merkel) + DFS + Recursion, Complexity: O(n), O(h)
    # Tip: Hash every subtree in the tree and store every subtree's hash in its
    #      respective root i.e. merkel hashing. The given subtree can only exist
    #      in the main tree if its hash is present in the main tree.

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Better hash function.
        def get_hash(s: str):
            hash = sha256()
            hash.update(s.encode())
            return hash.hexdigest()

        def hashTree(node: Optional[TreeNode]):
            # Base case: Null encountered.
            if not node:
                return ''

            # Hash of node = hash of left subtree + hash of node's value + hash of right subtree.
            node.hash = get_hash(hashTree(node.left) + get_hash(str(node.val)) + hashTree(node.right))
            return node.hash

        def findHash(node: Optional[TreeNode], target: str):
            if not node:
                return False

            # Check if current subtree (with current node as root) is the desired
            # subtree. If not, find the desired subtree in the left and right
            # subtrees of the current subtree.
            return node.hash == target or findHash(node.left, target) or findHash(node.right, target)

        # Hash the main tree.
        hashTree(root)
        # Find hash of subtree to be found.
        subhash = hashTree(subRoot)
        # Find the desired hash in the main tree.
        return findHash(root, subhash)
