class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = j = layer = 0
        traversal = []
        rows = len(matrix)
        cols = len(matrix[0])

        # define the four directions
        dirs = {
            'right': (0, 1),
            'down': (1, 0),
            'left': (0, -1),
            'up': (-1, 0),
        }
        curdir = 'right'

        while (len(traversal) < rows * cols):
            traversal.append(matrix[i][j])

            # change direction after processing last element in current direction
            if curdir == 'right' and j == cols - 1 - layer:
                curdir = 'down'
            elif curdir == 'down' and i == rows - 1 - layer:
                curdir = 'left'
            elif curdir == 'left' and j == 0 + layer:
                # cut down the movement area by one before moving "up" to create a spiral
                layer += 1
                curdir = 'up'
            elif curdir == 'up' and i == 0 + layer:
                curdir = 'right'

            # move in the current direction
            i += dirs[curdir][0]
            j += dirs[curdir][1]

        return traversal
