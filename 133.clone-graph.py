"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional

# Approach: DFS + Recursion + Hashmap, Complexity: O(n), O(n)
class Solution:
    # Hashmap to keep track of cloned nodes.
    def __init__(self):
        self.cloned = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Edge case: Empty graph.
        if not node:
            return None

        # Create a clone of the given node and record the cloned node in hashmap.
        clone = Node(node.val)
        self.cloned[node.val] = clone

        # Iterate over all nodes adjacent to the given node.
        for adj in node.neighbors:
            # If the adjacent node is not cloned yet, clone it and then add it as
            # neighbour of just cloned node.
            if adj.val not in self.cloned:
                clone.neighbors.append(self.cloneGraph(adj))
            # If the adjacent node is already cloned, add its reference from
            # hashmap as the neighbour of just cloned node.
            else:
                clone.neighbors.append(self.cloned[adj.val])

        # Return cloned node to parent call so that it can be added as adjacent
        # to node cloned in parent call.
        return clone
