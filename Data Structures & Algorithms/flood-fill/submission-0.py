class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        # base case     
        if original_color == color:
            return image

        def dfs(row, col):
            # 1. check bounds
            if row < 0 or row >= len(image):
                return
            if col < 0 or col >= len(image[0]):
                return
            
            # 2. check whether this cell has the original color
            # only cells with original color are recolored
            if image[row][col] != original_color:
                return 

            # 3. recolor this cell
            image[row][col] = color
            
            # 4. recurse up, down, left, right
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1) 

        dfs(sr, sc)

        return image