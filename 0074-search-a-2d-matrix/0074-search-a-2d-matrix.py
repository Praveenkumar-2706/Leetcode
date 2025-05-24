class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = (m * n)-1


        while low <= high:
            mid = (low + high) / 2
            row = mid / n
            col = mid % n
            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            if mid_val < target:
                low = mid+1
            if mid_val > target:
                high = mid - 1
        return False

        
        
        