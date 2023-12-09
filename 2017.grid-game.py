# Approach: Prefix Sum, Complexity: O(n), O(1)
# Tip: Greedy won't work here. Maximizing first robot != Minimizing second robot.
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        i = 1
        # Build prefixes for faster range sum calculation.
        while i < cols:
            grid[0][i] += grid[0][i-1]
            grid[1][i] += grid[1][i-1]
            i += 1

        # Once the first robot takes a particular path to the a[1][n-1], the
        # second robot can collect either:
        # i) points in the top row after the descent (d) of first robot.
        #    i.e. a[d+1] .. a[n-1] (or 0 if d = n)
        # ii) points in the bottom row before the descent (d) of first robot.
        #     i.e. a[0] .. a[d-1] (or 0 if d = 0)

        res = float('inf')
        for i in range(cols):
            # Second robot needs to choose local maxima of both sets of
            # collectable points to play optimally.
            points_right = grid[0][cols-1] - grid[0][i]
            points_left = grid[1][i-1] if i > 0 else 0
            second_robot = max(points_left, points_right)

            # First robot needs to move down at an index which leads to global
            # minima of points collected by second robot to play optimally.
            res = min(res, second_robot)
        return res
