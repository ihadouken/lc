class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        M = len(grid)
        N = len(grid[0])

        def dfs(x, y) -> int:
            if (x, y) in visited:
                return 0

            if x < 0 or y < 0 or x >= M or y >= N:
                return 1
            if not grid[x][y]:
                return 1

            visited.add((x, y))
            return dfs(x, y+1) + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1)

        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if grid[x][y]:
                    return dfs(x, y)

        return 0
