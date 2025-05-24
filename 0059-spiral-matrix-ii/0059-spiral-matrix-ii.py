class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0 or n > 20:
            return

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        top,left = 0,0
        bottom,right = n-1,n-1
        count = 0

        while count != n*n:
            for col in range(left,right+1):
                matrix[top][col] = count+1
                count+=1
            top += 1

            for row in range(top,bottom+1):
                matrix[row][right] = count+1
                count+=1
            right -= 1

            if top <= bottom:
                for col in range(right,left-1,-1):
                    matrix[bottom][col]=count+1
                    count+=1
                bottom -= 1

            if left <= right:
                for row in range(bottom,top-1,-1):
                    matrix[row][left] = count+1
                    count+=1
                left += 1
        return matrix 