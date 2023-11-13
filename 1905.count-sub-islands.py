class Solution:
    # Approach: DFS + Recursion, Complexity: O(mn), O(mn)
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        M = len(grid1)
        N = len(grid1[0])

        # Recursion DFS to explore an island while checking it its a subisland.
        def visit(x: int, y: int) -> bool:
            # If the bounds of the island or the grid itself (grid2) is reached,
            # assume the island is a subisland.
            if x < 0 or y < 0 or x >= M or y >= N or grid2[x][y] != 1:
                return True

            # Mark the current land square as visited.
            grid2[x][y] = -1
            res = True

            # If there is no corresponding land square in grid1, the assumption
            # is wrong. But, still its important to proceed with exploration.
            if grid1[x][y] == 0:
                res = False

            # Ensure that the subisland assumption is correct for the current
            # land square and its neighbouring land squares (effectively the
            # whole island) while carefully not short-circuiting the boolean
            # logic which causes partial exploration of island.
            res = visit(x, y+1) and res
            res = visit(x, y-1) and res
            res = visit(x+1, y) and res
            res = visit(x-1, y) and res
            return res

        # Iterate over grid2 and inc. count if an unexplored island is subisland.
        count = 0
        for i, row in enumerate(grid2):
            for j, square in enumerate(row):
                if square == 1 and visit(i, j):
                    count += 1

        # Return count of subislands.
        return count

