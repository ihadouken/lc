class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        # all rows starting from second
        for i in range(numRows-1):
            # every row starts with a 1
            row = [1]
            # get row elements by summing elements in previous row
            for j in range(i):
                row.append(prev_row[j] + prev_row[j+1])
            # every row ends with a 1
            row.append(1)
            triangle.append(row)
            prev_row = row
        return triangle
