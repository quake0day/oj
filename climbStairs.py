class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n <= 1:
        	return 1
        f = [0] * n
        f[0] = 1
        f[1] = 2
        for i in xrange(2,n):
        	f[i] = f[i-1] + f[i-2]
        return f[-1]

a = Solution()
print a.climbStairs(3)