class Solution(object):
    def hammingWeight(self, n):
        """ using Brian Kernighan's Algorithm"""
        count = 0;
        while(n != 0):
            n = n & (n-1)
            count += 1
        return count
        