class Solution(object):
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        newMatrix = [[0] * rows for _ in range(cols)]
        for i in range(0,rows):
            for j in range(0,cols):
                newMatrix[j][i] = matrix[i][j]
        return newMatrix

        