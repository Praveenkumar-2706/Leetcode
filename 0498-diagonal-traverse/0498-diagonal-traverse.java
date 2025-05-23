// import java.util.ArrayList;
// import java.util.List;

public class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        int[] res = new int[rows * cols];

        int curRow = 0, curCol = 0, idx = 0;
        boolean goingUp = true;

        while (idx < rows * cols) {
            if (goingUp) {
                while (curRow >= 0 && curCol < cols) {
                    res[idx++] = mat[curRow][curCol];
                    curRow--;
                    curCol++;
                }
                if (curCol == cols) {
                    curCol--;
                    curRow += 2;
                } else {
                    curRow++;
                }
                goingUp = false;
            } else {
                while (curRow < rows && curCol >= 0) {
                    res[idx++] = mat[curRow][curCol];
                    curRow++;
                    curCol--;
                }
                if (curRow == rows) {
                    curRow--;
                    curCol += 2;
                } else {
                    curCol++;
                }
                goingUp = true;
            }
        }

        return res;
    }
}
