class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        traversal = []
        direction = 1
        rows = len(mat)
        cols = len(mat[0])

        # Time: O(mn), Space: O(1))
        i = j = 0
        for _ in range(rows + cols - 1):
            while i >= 0 and j >= 0 and i < rows and j < cols:
                traversal.append(mat[i][j])
                i -= direction
                j += direction

            # bring indices back in range
            i += direction
            j -= direction

            # move to next diagonal's head opposite to last one
            if direction == 1:
                i += (j == cols-1)
                j += (j < cols-1)
            else:
                j += (i == rows-1)
                i += (i < rows-1)
            # reverse the traversal direction
            direction = -direction

        # Time: O(mn), Space: O(min(m, n))
        # i0 = j0 = 0
        # # traverse each diagonal
        # for _ in range(rows + cols - 1):
        #     i = i0
        #     j = j0
        #     diagonal = []
        #
        #     while j >= 0 and i < rows:
        #         diagonal.append(mat[i][j])
        #         i += 1
        #         j -= 1
        #
        #     # reverse every alternate diagonal starting from first
        #     if direction == 1:
        #        diagonal.reverse()
        #     traversal.extend(diagonal)
        #
        #     # calculate position of start of next diagonal
        #     if j0 == cols - 1:
        #         i0 += 1
        #     else:
        #         j0 += 1
        #
        #     direction = -direction

        return traversal
