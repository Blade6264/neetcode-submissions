class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # this uses dict
        sudoku_box = {}
        sudoku_row = {}
        sudoku_col = {}
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    pos_tuple = (int(i/3), int(j/3))
                    if pos_tuple not in sudoku_box:
                        sudoku_box[pos_tuple] = set(board[i][j])
                    else:
                        if board[i][j] in sudoku_box.get(pos_tuple):
                            return False
                        else:
                            sudoku_box[pos_tuple].add(board[i][j])

                    if i not in sudoku_row:
                        sudoku_row[i] = set(board[i][j])
                    else:
                        if board[i][j] in sudoku_row.get(i):
                            return False
                        else:
                            sudoku_row[i].add(board[i][j])

                    if j not in sudoku_col:
                        sudoku_col[j] = set(board[i][j])
                    else:
                        if board[i][j] in sudoku_col.get(j):
                            return False
                        else:
                            sudoku_col[j].add(board[i][j])
        return True
