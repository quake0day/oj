class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        f = []
        f.append(0)
        f.append(1)
        if n < 2 and n >= 0:
        	return f[n]
        elif n < 0:
        	return 0
        for i in xrange(2,n):
        	f.append(f[i-1] + f[i-2])
        return f[n-1]


a = Solution()
print a.fibonacci(10)

