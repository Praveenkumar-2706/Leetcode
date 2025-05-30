class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []

        top, left = 0,0
        bottom, right = rows-1,cols-1

        # while left <= right and top <= bottom:
        while len(res) != rows * cols:
            for col in range(left,right+1):
                res.append(matrix[top][col])
            top += 1

            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for col in range(right,left-1,-1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            
            if left <= right:
                for row in range(bottom,top-1,-1):
                    res.append(matrix[row][left])
                left += 1
        return res