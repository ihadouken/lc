class Solution:
    def isValidSudoku(self, board) -> bool:
        # # Validate rows
        # for i in range(9):
        #     seen = set()
        #     for j in range(9):
        #         element = board[i][j]
        #         if element in seen:
        #             return False
        #         if element != '.':
        #             seen.add(element)
        #
        # # Validate columns
        # for j in range(9):
        #     seen = set()
        #     for i in range(9):
        #         element = board[i][j]
        #         if element in seen:
        #             return False
        #         if element != '.':
        #             seen.add(element)
        #
        # # Validate compartments
        # for i0 in range(3):
        #     for j0 in range(3):
        #         seen = set()
        #         for i in range(3):
        #             for j in range(3):
        #                 element = board[i0*3 + i][j0*3 + j]
        #                 if element in seen:
        #                     return False
        #                 if element != '.':
        #                     seen.add(element)

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    boxid = (i//3)*3 + j//3
                    if element in rows[i] or element in cols[j] or element in boxes[boxid]:
                        return False

                    rows[i].add(element)
                    cols[j].add(element)
                    boxes[boxid].add(element)
        return True
