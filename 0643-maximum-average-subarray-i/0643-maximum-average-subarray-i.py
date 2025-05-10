# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         n = len(nums)
#         curr_sum = 0

#         for i in range(k):
#             curr_sum += nums[i]

#         max_avg = curr_sum/k

#         for i in range(k, n):
#             curr_sum += nums[i]
#             curr_sum -= nums[i - k]

#             avg = curr_sum/float(k)
#             max_avg = max(max_avg, avg)
#         return max_avg

class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        curr_sum = sum(nums[:k])  # Compute the sum of the first 'k' elements
        max_avg = curr_sum / float(k)  # Ensure floating-point division

        for i in range(k, n):
            curr_sum += nums[i] - nums[i - k]  # Sliding window update
            max_avg = max(max_avg, curr_sum / float(k))  # Update max average

        return max_avg
