# Approach: Prefix Sum
class NumMatrix:
    # Complexity: O(m*n)
    def __init__(self, matrix: List[List[int]]):
        # Build a prefix matrix that builds running sum horizontally + vertically
        # at the same time i.e. diagonally. Thus, every submatrix's sum is stored
        # in its bottom-right element. Have extra first row and first column of
        # zeroes to avoid edge cases where there is no element on top/left of
        # element. Due to this, indices have to be offset by +1.

        # For example,
        #   a    b       a          a+b
        #           ->
        #   c    d      a+c   (a+b) + (a+c) - a

        self.prefix = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                self.prefix[i+1][j+1] = self.prefix[i][j+1] + self.prefix[i+1][j] + matrix[i][j] - self.prefix[i][j]

    # Complexity: O(1)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Return the sum of required region, by decrementing region outside left
        # and top margins from the submatrix top-left origin and bottom-right
        # (row2, col2). Since the region outside both margins is decremented
        # twice, make up for it by adding it back once.
        return self.prefix[row2+1][col2+1] - self.prefix[row2+1][col1] - self.prefix[row1][col2+1] + self.prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
