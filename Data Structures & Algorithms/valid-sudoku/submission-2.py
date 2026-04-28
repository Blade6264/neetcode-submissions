class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialize the dict with key: None and value: empty set 
        sudoku_box = defaultdict(set)
        sudoku_row = defaultdict(set)
        sudoku_col = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val.isdigit():
                    pos_tuple = (int(i/3), int(j/3))
                    # my_defaultdict.get or my_dict.get will raise error if the key is not found in the dict/defaultdict
                    # while my_defaultdict[key] and my_dict[key] won't
                    # they will instead create a new key and value pair
                    if val in sudoku_box[pos_tuple] or val in sudoku_row[i] or val in sudoku_col[j]:
                        return False
                    sudoku_box[pos_tuple].add(val)
                    sudoku_row[i].add(val)
                    sudoku_col[j].add(val)
        return True