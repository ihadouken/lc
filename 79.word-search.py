class Solution:
    # Approach: DFS + Backtracking + Recursion + Hashset, Complexity: O((m*n)^2), O(m*n)
    # Note: There might be a traversal of the whole grid for each element in the
    #       worst case, hence the TC. If all chars have to be used to get the
    #       word, the recursive stack may warrant O(m*n) space.

    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])

        # Use set to keep track of cells that have been used once.
        used = set()
        # There are four cells adjacent to each cell.
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(x: int, y: int, wordi: int) -> bool:
            # If the cell is already used or doesn't contain the desired char,
            # try another option.
            if (x, y) in used or board[x][y] != word[wordi]:
                return False

            # If the last char has just been found, terminate the search.
            if wordi+1 == len(word):
                return True

            # Mark the found char as used for now.
            used.add((x, y))

            # Try finding next char among its neighbours. Multiple such
            # neighbours are all potential options to complete search.
            for dx, dy in dirs:
                newx, newy = x + dx, y + dy
                if 0 <= newx < M and 0 <= newy < N and dfs(newx, newy, wordi+1):
                    return True

            # If the search was unsuccessful using this cell, release it before
            # backtracking and trying out other options provided by its parent.
            used.remove((x, y))
            return False

        # Try searching the word assuming each cell as starting (one at a time).
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if dfs(i, j, 0):
                    return True

        # If none of the searches were successful, word doesn't exist in grid.
        return False
