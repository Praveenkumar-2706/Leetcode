class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int sum = 0;
        int minLength = Integer.MAX_VALUE;
        for (int right = 0; right < nums.length; right++){
            sum += nums[right];
            while(sum >= target){
                if(right-left+1 < minLength){
                    minLength = right - left + 1;
                }
                sum -= nums[left];
                left++;
            }
        }
        return minLength != Integer.MAX_VALUE?minLength:0;
    }
}