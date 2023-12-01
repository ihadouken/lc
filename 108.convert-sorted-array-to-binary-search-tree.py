# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Approach: Divide & Conquer, Complexity: O(nlogn), O(logn)
    # Tip: The height of a BST is minimized if it is the middle element in the
    #      sorted array. Again, heights of root's left and right subtrees are
    #      minimized if the middle elements of the partitions 0..m-1 and m+1..n-1
    # are chosen as left and right children respectively. This rule is valid for
    # all subtrees and array partitions at mid recursively.

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make_tree(nums, beg, end):
            # If an empty partion is produced, make previous node a leaf node.
            if beg > end:
                return None

            # Find middle of the subarray and create a tree node out of it.
            mid = (beg + end) // 2
            node = TreeNode(nums[mid])

            # Insert the middle of left and right partitions (division via "mid")
            # as left and right children respectively. Do this step recursively
            # for every partition until an empty partition i.e. leaf node is found.
            node.left = make_tree(nums, beg, mid-1)
            node.right = make_tree(nums, mid+1, end)

            # Return the node to its parent's call to make it the parent's child.
            return node

        # Initiate recursion by calling the recursive function on input array.
        return make_tree(nums, 0, len(nums)-1)
