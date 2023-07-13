class Solution:
    # Complexity - Time: O(mn), Space: O(sum(wall[0]))
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Remember passes for each column. Total columns = sum(wall[0]) - 1 as
        # we can draw the line along the edges of the wall.
        passes = {}

        # There is a clean pass after every brick in the row i.e. we can pass
        # freely at every column equal to cummulative brick width at any point
        # for a row.
        for brick_row in wall:
            width = 0
            # We can't pass after the last brick so one less iteration.
            for brick in range(len(brick_row)-1):
                width += brick_row[brick]
                # One more clean pass for the column.
                passes[width] = passes.get(width, 0) + 1

            # Maximising clean passes minimises crossed brickes naturally.
            max_passes = max(passes.values()) if passes else 0

        # Bricks crossed = total rows - clean passes
        return len(wall) - max_passes

