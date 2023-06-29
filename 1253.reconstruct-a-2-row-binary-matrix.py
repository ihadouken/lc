class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        urow = []
        lrow = []

        for i, sum in enumerate(colsum):
            if sum == 2:
                urow.append(1)
                lrow.append(1)
                upper -= 1
                lower -= 1
            elif sum == 0:
                urow.append(0)
                lrow.append(0)
            else:
                if upper >= lower:
                    urow.append(1)
                    lrow.append(0)
                    upper -= 1
                else:
                    lrow.append(1)
                    urow.append(0)
                    lower -= 1

        if upper == 0 and lower == 0:
            return [urow, lrow]
        return []
