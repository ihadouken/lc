class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        special = 0

        # Use auxillary arrays to store count of ones in rows & columns.
        row_counts = [0] * M
        col_counts = [0] * N

        # Iterate over matrix and compute count of ones in rows & columns.
        for i, row in enumerate(mat):
            for j, element in enumerate(row):
                if element:
                    row_counts[i] += 1
                    col_counts[j] += 1

        # For a position to be special it must be the only 1 in its row and
        # column i.e. count of ones in its row and column must be 1.
        for i, row in enumerate(mat):
            for j, element in enumerate(row):
                if element and row_counts[i] == 1 and col_counts[j] == 1:
                    special += 1

        # Return number of special positions.
        return special
