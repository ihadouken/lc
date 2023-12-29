class Solution:
    # Approach: Two Pointer, Complexity: O(m+n), O(1)
    def countNegatives(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        pivot, res = 0, 0

        # Start at the upper right corner of the matrix.
        j = cols - 1

        # Scan the grid top to bottom.
        for row in grid:
            # Keep going left to find the first +ve element.
            while j >= 0 and row[j] < pivot:
                j -= 1

            # Count elements < 0 using index of first +ve.
            res += cols - (j+1)

            # Move to the row below and find its 1st +ve which can't be at some
            # index > j because a[i-1][j+1] < 0 and a[i][j+1] < a[i-1][j+1].

        # Return sum of all elements counted < 0.
        return res
