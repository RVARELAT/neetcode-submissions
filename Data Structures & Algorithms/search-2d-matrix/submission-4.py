class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # make left and right pointer for rows and determine which row to search
        # then run normal binary serach on row
        
        left = 0
        # matrix[0]
        right = len(matrix) - 1
        # matrix[len(matrix) - 1]
        
        while left <= right:
            # middle row
            mid = (left + right) // 2
            
            # target is in the first rows before middle
            if target < matrix[mid][0]:
                right = mid - 1
            # target is in rows after middle
            elif target > matrix[mid][0] and target > matrix[mid][len(matrix[mid]) - 1]:
                left = mid + 1
            # we found the row where target SHOULD be in, search row using bianry search
            else:
                target_row = matrix[mid]
                
                left = 0
                right = len(target_row) - 1
                
                while left <= right:
                    mid = (left + right) // 2
                    
                    if target == target_row[mid]:
                        return True
                    # target is on left side
                    elif target < target_row[mid]:
                        right = mid - 1
                    else:
                    # target is on right side
                        left = mid + 1
                
                # target is not in row it should be in
                return False
        
        return False