class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # helper template for counting digits
        digits_template = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}

        # create a hashtable for rows
        # ----- check rows -----
        for row in board:
            row_hash = digits_template.copy()
            for v in row:
                if v == ".":
                    continue
                row_hash[v] += 1
                if row_hash[v] > 1:
                    return False
        

        # ----- check columns -----
        for col_index in range(9):
            col_hash = digits_template.copy()
            for row_index in range(9):
                v = board[row_index][col_index]        # ✅ correct indexing
                if v == ".":
                    continue
                col_hash[v] += 1
                if col_hash[v] > 1:
                    return False
                
                
        # ----- check 3×3 squares -----
        # iterate the top-left anchors of each 3×3 box: (0,0), (0,3), (0,6), (3,0), ...
        for box_row in (0, 3, 6):
            for box_col in (0, 3, 6):
                square_hash = digits_template.copy()
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        v = board[r][c]                # ✅ actual cell value
                        if v == ".":
                            continue
                        square_hash[v] += 1
                        if square_hash[v] > 1:
                            return False

        return True


# 🕒 Time Complexity: O(n²)
# You iterate over every cell in a 9×9 grid → that’s n × n total.
# Each lookup and insert in a hash table is O(1) on average.
# You do three full passes (rows, columns, boxes), but constant factors don’t change the big-O.
# So overall → O(n²).
# 💾 Space Complexity: O(n)
# At any point, you only keep one hash table of size up to n (9 digits).
# You reuse it for each row, column, and box — not all at once.
# So your auxiliary memory grows linearly with n → O(n).
# (And for the fixed 9×9 Sudoku, that’s effectively constant space in practice.)
