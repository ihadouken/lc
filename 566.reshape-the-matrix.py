class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        r0 = len(mat)
        c0 = len(mat[0])
        if r0 * c0 != r * c:
            return mat

        reshape = [[]]
        i = j = 0

        for row in mat:
            for element in row:
                if j == c:
                    reshape.append([])
                    i += 1
                    j = 0
                reshape[i].append(element)
                j += 1
        return reshape
