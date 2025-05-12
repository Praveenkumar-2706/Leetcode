class Solution(object):
    memo = [0]*46
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        if Solution.memo[n] != 0:
            return Solution.memo[n]
        Solution.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return Solution.memo[n]
        