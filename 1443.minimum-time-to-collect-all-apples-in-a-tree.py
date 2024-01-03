class Solution:
    # Approach: Tree (Undirected) + DFS + Recursion, Complexity: O(n), O(h)
    # Tip: Add to cost moving bottom-up towards root only if current node or any
    #      descendant has an apple.

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Create an adjacency list out of the edge list.
        children = collections.defaultdict(list)
        for src, dest in edges:
            children[src].append(dest)
            children[dest].append(src)

        def collect(cur: int, parent: int) -> int:
            # Init cost = 0 as it is not known if traversing current node leads
            # to collection of any apples.
            cost = 0

            # Visit every child of current node.
            for child in children[cur]:
                # Avoid recursing back to the parent due to undirected tree.
                if child != parent:
                    # Sum cost of visiting descendants.
                    cost += collect(child, cur)

            # Pretend current node was never visited if current and all its
            # descendants collect zero apples in conjuction i.e. cost = 0.
            if hasApple[cur] or cost:
                return cost + 1
            return cost

        # Minus 1 from cost as collect() incorrectly includes root in calculation
        # of cost. Multiply cost by 2 to account for movement in both directions.
        # This may cause -ve cost when there are no apples in the tree so min = 0.
        total_cost = (collect(0, -1) - 1) * 2
        return max(0, total_cost)
