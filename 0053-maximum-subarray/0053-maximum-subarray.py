class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentsum = nums[0];
        maxsum = nums[0];
        for i in range(1,len(nums)):
            currentsum = max(currentsum+nums[i],nums[i])
            maxsum = max(maxsum,currentsum)
        return maxsum