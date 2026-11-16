class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if (num == "."):
                    continue
                if(num in rows[r]):
                    return False
                rows[r].add(num)

                if(num in cols[c]):
                    return False
                cols[c].add(num)

                box_index = (r//3)*3 + (c//3)

                if(num in squares[box_index]):
                    return False
                squares[box_index].add(num)

        return True
        
        