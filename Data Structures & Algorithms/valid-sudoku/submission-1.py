class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # these are hashmaps
        # key colum number
        # set is all values in that column
        # intializies default values to a set 
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)
        
        # iterate through the entire grid
        for r in range(9):
            for c in range(9):
                # check if empty, if so, skip
                if board[r][c] == ".":
                    continue # go to next interation of the loop
                # check if its a duplicate
                
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or   
                    # squares[(r // 3, c // 3)] will return a set of all values in that subsquare
                    board[r][c] in squares[(r // 3, c // 3)] ):        
                        return False 
                # if not a duplciate, we add this num in grid to our sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
