class Solution(object):
    def fib(self, n):
        ans=[0,1]
        for i in range(2,n+1):
            ans.append(ans[i-1]+ans[i-2])
        return ans[n]