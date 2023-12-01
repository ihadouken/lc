class Solution:
    # Approach: DFS + Recursion, Complexity: O(n), O(n)
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Sets to store already visited and known unsafe states.
        visit, unsafe = set(), set()
        # Store safe states in sorted order as indices of boolean array.
        safe = [False] * len(graph)

        def isSafe(node: int) -> bool:
            # If a nodes is safe any node reaching it might be safe.
            if safe[node]:
                return True

            # If a node reaches a visited non-safe node, it is part of a cycle
            # and is definitely unsafe.
            if node in unsafe or node in visit:
                unsafe.add(node)
                return False

            # Mark a node as visited.
            visit.add(node)

            # A node is safe if its has no neighbours or all of its neighbours
            # are safe.
            for neighbours in graph[node]:
                if not isSafe(neighbours):
                    unsafe.add(node)
                    return False

            # Mark the node as safe.
            safe[node] = True
            # Notify the parent call of its neighbour being safe.
            return True

        # Check safeness of each node in the graph.
        for node in range(len(graph)):
            isSafe(node)
        # Use boolean array's indices to return safe nodes in sorted format.
        return [i for i, is_safe in enumerate(safe) if is_safe]
