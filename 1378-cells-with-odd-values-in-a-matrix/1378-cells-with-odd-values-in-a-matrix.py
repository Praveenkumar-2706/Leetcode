class Solution(object):
    def oddCells(self, m, n, indices):
        row = [0] * m
        col = [0] * n

        # Count the number of times each row and column is incremented
        for r, c in indices:
            row[r] += 1
            col[c] += 1

        count = 0

        # For each cell, check if the total increments (row + col) is odd
        for i in range(m):
            for j in range(n):
                if (row[i] + col[j]) % 2 != 0:
                    count += 1

        return count
