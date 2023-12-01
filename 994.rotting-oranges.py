class Solution:
    # Approach: BFS, Complexity: O(m*n), O(m*n)
    # Tip: Find all cells where the rotting will start. Emulate the rotting done
    #      by every cell using BFS by adding next cells prone to rot by current
    #      rotten cell.

    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        depth = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = collections.deque()

        # Add all rotting epicentres to a queue.
        for i, row in enumerate(grid):
            for j, orange in enumerate(row):
                if orange == 2:
                    q.append([i, j, 0])


        # Do a BFS where a rotten cell rots its neighbour in an iteration. Cell
        # rotten first will rot its neighbours first (FIFO).
        while q:
            x, y, depth = q.popleft()

            for dx, dy in dirs:
                newx, newy = x + dx, y + dy

                # If a cell is in bounds and contains an orange, it can rot. So,
                # add it to queue to rot it later.
                if 0 <= newx < M and 0 <= newy < N and grid[newx][newy] == 1:
                    # Mark the cell rotting in the future as rotten, so its not
                    # added to queue multiple times.
                    grid[newx][newy] = 2
                    q.append([newx, newy, depth+1])

        # If any unrotten orange exists, the rotting has failed.
        for row in grid:
            for orange in row:
                if orange == 1:
                    return -1

        # Maximum depth of the BFS = Min time for all cells to rot.
        return depth
