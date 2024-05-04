class Queen(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def not_attack(row, col):
            for prev_row in range(row):
                if board[prev_row] == col or \
                board[prev_row] - prev_row == col - row or \
                board[prev_row] + prev_row == col + row:
                    return False
            return True

        def place_queen(row):
            if row == n:
                result.append(
                    ['.' * i + 'Q' + '.' * (n - i - 1) for i in board]
                    )
            else:
                for col in range(n):
                    if not_attack(row, col):
                        board[row] = col
                        place_queen(row + 1)
                        board[row] = -1 # Backtrack
    
        result = []
        board = [-1] * n # board to hold the column index of the queen in each row
        place_queen(0)
        return result