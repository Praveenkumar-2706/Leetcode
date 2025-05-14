class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        res = [0]*2
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    res[0] = i
                    res[1] = j
        return res

        
        