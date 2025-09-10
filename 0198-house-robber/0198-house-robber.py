class Solution(object):
    def rob(self, nums):
        sum1 = sum2 = 0
        # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         sum1 += nums[i]
        #     else:
        #         sum2 += nums[i]
        # return max(sum1,sum2)

        for i in nums:
            newsum1 = sum2 + i
            newsum2 = max(sum1,sum2)
            sum1,sum2 = newsum1,newsum2
        return max(sum1,sum2)
        