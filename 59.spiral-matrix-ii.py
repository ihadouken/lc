class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        layer = i = j = 0
        element = 1
        curdir = 'right'

        dirs = {
            'right': (0, 1),
            'down': (1, 0),
            'left': (0, -1),
            'up': (-1, 0),
        }
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        while (element <= n*n):
            matrix[i][j] = element
            element += 1

            if curdir == 'right' and j == n - 1 - layer:
                curdir = 'down'
            elif curdir == 'down' and i == n - 1 - layer:
                curdir = 'left'
            elif curdir == 'left' and j == 0 + layer:
                layer += 1
                curdir = 'up'
            elif curdir == 'up' and i == 0 + layer:
                curdir = 'right'

            i += dirs[curdir][0]
            j += dirs[curdir][1]

        return matrix
