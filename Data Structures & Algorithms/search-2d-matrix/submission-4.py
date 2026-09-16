class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)  #matrix[(1,2,4,8), (10, 11, 12, 13), (14, 20, 30, 40)] -> length = 3
        COLS = len(matrix[0]) #matrix[0] = (1,2,4,8) -> length = 4
        top = 0 
        bot = ROWS - 1 #2

        while top <= bot: 
            row = (top + bot) // 2
            
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        l, r = 0, COLS - 1

        while l <= r: 
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        return False

        
        
