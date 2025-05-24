class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        int low = 0, high = (m * n)-1;

        while(low <= high){
            int mid = (low + high) / 2;
            int row = mid / n;
            int col = mid % n;
            int mid_value = matrix[row][col];
            
            if(mid_value == target){
                return true;
            }
            if(mid_value > target){
                high = mid-1;
            }
            if(mid_value < target){
                low = mid+1;
            }
        }
        return false;
    }
}