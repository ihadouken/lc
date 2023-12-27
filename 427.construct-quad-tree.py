"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    # Approach: DFS, Recursion (bottom-up), Complexity: O(n), O(log4(n)) where
    # n -> number of elements in the grid. Each element is visited once. The
    # grid is divided into 4 parts at only part remains in stack at a time.

    def construct(self, grid: List[List[int]]) -> 'Node':
        # Base case: Only 1 element in grid i.e. certainly a leaf in quad tree.
        if len(grid) == 1:
            return Node(grid[0][0], 1, None, None, None, None)

        # Divide current grid into 4 parts and recursively process them.
        half = len(grid)//2
        topLeft = self.construct([row[:half] for row in grid[:half]])
        topRight = self.construct([row[half:] for row in grid[:half]])
        bottomLeft = self.construct([row[:half] for row in grid[half:]])
        bottomRight = self.construct([row[half:] for row in grid[half:]])

        # If four leaft nodes have same value, wrap them up into their parent.
        # This step eventually (bottom-up) groups equal elements into leaf subgrids.
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
            return Node(topLeft.val, 1, None, None, None, None)
        # Separate nodes are created for each child in case of no grouping.
        else:
            return Node(1, 0, topLeft, topRight, bottomLeft, bottomRight)
