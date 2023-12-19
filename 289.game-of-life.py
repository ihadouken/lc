from copy import deepcopy

class Solution:
    # Approach: Simulation + In-Place Operations, Complexity: O(m*n), O(1)
    # Tip: Encapsulate the state and neighbour count of cell in a single number.
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])

        # Cell is live if it has negative value. Otherwise, its dead.
        def getState(cell: int) -> int:
            if cell > 0:
                return 1
            return 0

        for i in range(m):
            for j in range(n):
                # Find the number of live cells adjacent to a cell. getState(x)
                # finds out if a cell is live/dead using the (cleverly) stored
                # neighbour count when the cell was accessed previously.
                ncount = getState(board[i-1][j-1]) if i != 0 and j != 0 else 0
                ncount += getState(board[i-1][j+1]) if i != 0 and j != n-1 else 0
                ncount += getState(board[i+1][j-1]) if i != m-1 and j != 0 else 0
                ncount += getState(board[i+1][j+1]) if i != m-1 and j != n-1 else 0

                ncount += getState(board[i][j-1]) if j != 0 else 0
                ncount += getState(board[i][j+1]) if j != n-1 else 0
                ncount += getState(board[i-1][j]) if i != 0 else 0
                ncount += getState(board[i+1][j]) if i != m-1 else 0

                # If a cell is live store -> neighbour count + 1.
                # If a cell is dead store -> -ve of neighbour count.
                if board[i][j] == 0:
                    board[i][j] = -ncount
                else:
                    board[i][j] = ncount + 1

        for i in range(m):
            for j in range(n):
                live = getState(board[i][j])
                # Need to take abs because neighbour count is negative for dead.
                # Subtract 1 only if cell is alive (positive neighbout count).
                ncount = abs(board[i][j]) - live

                # Restore the cell value as original (0 for dead, 1 for live).
                board[i][j] = live

                # Check if there is over/under population.
                if live and (ncount < 2 or ncount > 3):
                    board[i][j] = 0

                # Check if there is reproduction.
                elif not live and ncount == 3:
                    board[i][j] = 1

    # Approach: Simulation, Complexity: O(m*n), O(m*n)
    # def gameOfLife(self, board: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     # Create a copy of the board for modifications.
    #     new = deepcopy(board)
    #     # new = [row[:] for row in board]
    #     m = len(board)
    #     n = len(board[0])
    #
    #     for i in range(m):
    #         for j in range(n):
    #             # Count neighbour cells that are populated. Before accessing a
    #             # potential neighbour cell, ensure that it even exists to avoid
    #             # "index out of range".
    #             count = board[i-1][j-1] if i != 0 and j != 0 else 0
    #             count += board[i-1][j+1] if i != 0 and j != n-1 else 0
    #             count += board[i+1][j-1] if i != m-1 and j != 0 else 0
    #             count += board[i+1][j+1] if i != m-1 and j != n-1 else 0
    #
    #             count += board[i][j-1] if j != 0 else 0
    #             count += board[i][j+1] if j != n-1 else 0
    #             count += board[i-1][j] if i != 0 else 0
    #             count += board[i+1][j] if i != m-1 else 0
    #
    #             # Check cells near a live cell for under/over population.
    #             if new[i][j] == 1 and (count < 2 or count > 3):
    #                 new[i][j] = 0
    #             # Check for reproduction near a dead cell.
    #             elif new[i][j] == 0 and count == 3:
    #                 new[i][j] = 1
    #
    #     # Write new state for each cell one-by-one in the input.
    #     for i in range(m):
    #         for j in range(n):
    #             board[i][j] = new[i][j]
