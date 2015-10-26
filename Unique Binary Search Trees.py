class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
        count = [0] * (n+1)
        count[0] = 1
        count[1] = 1
        for i in xrange(2, n+1):
        	for j in xrange(i):
        		count[i] += count[j] * count[i-j-1]
        return count[n]
