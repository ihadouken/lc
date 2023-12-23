class Solution:
    # Approach: DFS + Recursion + Reverse Thinking, Complexity: O(mn), O(mn)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Create sets to store nodes reachable from atlantic and pacific.
        atlantic, pacific = set(), set()
        M = len(heights)
        N = len(heights[0])

        # Use DFS to find all nodes reachable from a given node.
        def dfs(x: int, y: int, reachable: set) -> None:
            reachable.add((x, y))
            dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

            # Try all of current square's neighbours if any of them are reachable.
            for dx, dy in dirs:
                newx, newy = x + dx, y + dy
                # If a neighbour (newx, newy) is valid and water can reach the
                # square (x, y) from it.
                if 0 <= newx < M and 0 <= newy < N and heights[newx][newy] >= heights[x][y] and (newx, newy) not in reachable:
                    # DFS on it to add it to the set and check its neighbours.
                    dfs(newx, newy, reachable)

        # Store cells reachable from all four boundaries using correct ocean st.
        for i in range(0, M):
            # Left boundary
            dfs(i, 0, pacific)
            # Right boundary
            dfs(i, N-1, atlantic)
        for j in range(0, N):
            # Top boundary
            dfs(0, j, pacific)
            # Bottom boundary
            dfs(M-1, j, atlantic)

        # Find squares reachable from both pacific and atlantic and convert set
        # of tuples to list of lists.
        return list(map(list, list(pacific.intersection(atlantic))))
