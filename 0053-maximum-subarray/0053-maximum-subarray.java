class Solution {
    public int maxSubArray(int[] nums) {
        int sum_ = nums[0];
        int maxsum = nums[0];
        for (int i = 1; i < nums.length; i++){
            sum_ = Math.max(nums[i],sum_+nums[i]);
            maxsum = Math.max(maxsum,sum_);
        }
        return maxsum;

        // int sum = nums[0];
        // int maxsum = nums[0];
        // for (int i = 0; i < nums.length; i++){

        // }
        // for (int j = 1; j<nums.length;j++){
        //     sum
        // }
    }
}