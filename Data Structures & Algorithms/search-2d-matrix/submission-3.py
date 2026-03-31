class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # perform binary search to find the row to search on
        # look through first element of each row
        left_rows = 0
        right_rows = len(matrix) - 1
        
        while left_rows <= right_rows:
            mid_rows = (left_rows + right_rows) // 2
            
            if target >= matrix[mid_rows][0] and target <= matrix[mid_rows][-1]:
                # matrix[mid] is the row we want to search through
                row = matrix[mid_rows]
                # perform binary search on row
                left = 0 
                right = len(row) - 1

                while left <= right:
                    mid = (left + right) // 2
                    # found target
                    if row[mid] == target:
                        return True
                    # num at mid is bigger than target, search left side, move right pointer 1 before mi
                    elif row[mid] > target:
                        right = mid - 1
                    else:
                        # num at mid is less than target, search right side
                        left = mid + 1
                
                # element not found at possible row it shuld be found
                return False
            
            # num at mid is bigger than target, search left side, move right pointer 1 before mi
            elif matrix[mid_rows][0] > target:
                right_rows = mid_rows - 1
                
            else:
                # num at mid is less than target, search right side
                left_rows = mid_rows + 1
        
        # target not found
        return False

# ⏱ Time Complexity: O(log m + log n)
# First, you do a binary search over the rows to find which row the target could be in → O(log m)
# Then, you do another binary search within that row → O(log n)
# Add them together → O(log m + log n), which is the same as O(log (m × n)).
# ✅ In simple words:
# You cut the number of rows in half each step,
# then you cut the number of elements in that row in half again.

# 💾 Space Complexity: O(1)
# You only use a few variables (left, right, mid, etc.) —
# no extra data structures or copies of the matrix.
# ✅ In simple words:
# The algorithm only keeps track of a few pointers,
# so it uses constant memory regardless of matrix size.

# 🔹 The rule
# log(a×b)=log(a)+log(b)
# That’s one of the basic logarithm identities.
# It means adding two logs is the same as taking the log of their product.
            

# O(m * log(n)) solution  
            
    # #while left_row <= right_row
    
    # for row in matrix:
    #     # binary search at each row
    #     left = 0 
    #     right = len(row) - 1
        
    #     while left <= right:
    #         mid = (left + right) // 2
    #         # found target
    #         if row[mid] == target:
    #             return True
    #         # num at mid is bigger than target, search left side, move right pointer 1 before mi
    #         elif row[mid] > target:
    #             right = mid - 1
    #         else:
    #             # num at mid is less than target, search right side
    #             left = mid + 1
    # return False