class Solution:
    # Approach: DFS, Complexity: O(m*n), O(m*n)
    # Tip: Think in reverse. Any O regions eventually connecting to a O on the
    #      boundary are unsurrounded. Trace and mark all those O regions via dfs
    #      from boundary Os.

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])

        def visit(x: int, y: int) -> None:
            # DFS base case: Out of bounds.
            # DFS base case: Marked O or X encountered.
            if x < 0 or y < 0 or x >= M or y >= N or board[x][y] != 'O':
                return

            # Any O reached from boundary O is unsurrounded. Mark it.
            board[x][y] = 'U'

            # Neighbours Os of marked O make up the rest of unsurrounded region.
            visit(x-1, y)
            visit(x+1, y)
            visit(x, y-1)
            visit(x, y+1)

        # Execute above DFS on all Os in first and last column.
        for i in range(0, M):
            if board[i][0] == 'O':
                visit(i, 0)
            if board[i][N-1] == 'O':
                visit(i, N-1)

        # Execute above DFS on all Os in first and last row.
        for j in range(0, N):
            if board[0][j] == 'O':
                visit(0, j)
            if board[M-1][j] == 'O':
                visit(M-1, j)

        for i, row in enumerate(board):
            for j, square in enumerate(row):
                # All marked Os (reachable from boundary Os) are unsurrounded.
                if square == 'U':
                    board[i][j] = 'O'
                # All unmarked Os (unreachable from boundary Os) are surrounded.
                elif square == 'O':
                    board[i][j] = 'X'
