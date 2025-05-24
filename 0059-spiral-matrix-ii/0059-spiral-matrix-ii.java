class Solution {
    public int[][] generateMatrix(int n) {
        if(n <= 0 || n > 20){
            return null;
        }
        int[][] matrix = new int[n][n];
        int top = 0,left = 0;
        int bottom = n-1,right = n-1;
        int count = 0;

        while(count != (n*n)){
            for(int col=left;col < right + 1;col++){
                matrix[top][col] = count+1;
                count++;
            }
            top++;

            for(int row=top;row < bottom + 1;row++){
                matrix[row][right] = count+1;
                count++;
            }
            right--; 

            if(top <= bottom){
                for(int col=right;col > left - 1;col--){
                matrix[bottom][col] = count+1;
                count++;
            }
            bottom--;
            }

            if(left <= right){
                for(int row=bottom;row > top - 1;row--){
                matrix[row][left] = count+1;
                count++;
            }
            left++;
            }       
        }
        return matrix;
    }
}