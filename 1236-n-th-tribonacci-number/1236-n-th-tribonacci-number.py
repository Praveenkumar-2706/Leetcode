class Solution(object):
    memo = [0]*38

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if Solution.memo[n] != 0:
            return Solution.memo[n]
        Solution.memo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return Solution.memo[n]
