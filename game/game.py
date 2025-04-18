class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_symbol = "X"
        self.winner = None
        self.moves = 0

    def make_move(self, row, col):
        if self.board[row][col] != " " or self.winner:
            return False

        self.board[row][col] = self.current_symbol
        self.moves += 1

        if self.check_winner(row, col):
            self.winner = self.current_symbol
        else:
            self.current_symbol = "O" if self.current_symbol == "X" else "X"

        return True

    def check_winner(self, row, col):
        symbol = self.current_symbol
        board = self.board

        win_row = all(board[row][c] == symbol for c in range(3))
        win_col = all(board[r][col] == symbol for r in range(3))
        win_diag1 = all(board[i][i] == symbol for i in range(3))
        win_diag2 = all(board[i][2 - i] == symbol for i in range(3))

        return win_row or win_col or win_diag1 or win_diag2

    def is_draw(self):
        return self.moves == 9 and not self.winner

    def get_status(self):
        return {
            "board": self.board,
            "current_symbol": self.current_symbol,
            "winner": self.winner,
            "draw": self.is_draw()
        }
