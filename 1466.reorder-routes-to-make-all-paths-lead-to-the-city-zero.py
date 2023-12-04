class Solution:
    # Approach: Graph (weighted) + DFS + Recursion, Complexity: O(n), O(n)
    # Tip: Treat every edge as undirected (bidirectional). Original and artificial
    #      (reversed) edges have weights 1 and 0 respectively as when descending
    #      the tree-like structure from root 0, using a artificial edge has cost 0
    #      as this means that the original edge pointed upwards (towards root)
    #      thus needing no reversal. But, using an original edge has cost 1 as it
    #      means that original edge points downwards (away from root) and thus
    #      the edge needs to be reversed.

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.cost = 0
        # Use adjacency lists for each node to represent graph.
        adj = [[] for _ in range(n)]

        # Create undirected graph out of given edges.
        for src, dest in connections:
            adj[src].append((dest, 1))
            adj[dest].append((src, 0))

        def dfs(cur: int, parent: int) -> None:
            # Iterate over all children of a node.
            for child, weight in adj[cur]:
                # Avoid traversing back to a node's parent (by using a edge
                # complementing the edge used to originally reach it).
                if child != parent:
                    # Increment cost according to type of edge used.
                    self.cost += weight
                    # Recurse on the traversed child.
                    dfs(child, cur)

        # Initiate DFS on the root i.e. city 0.
        dfs(0, -1)
        # Return the traversal cost.
        return self.cost
