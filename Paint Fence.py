class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        allRes = []
        res = []
        if k == 0 or n == 0: return 0
        if n == 1: return 1
        res[0] = 1
        for i in xrange(1,n):
        	for j in xrange(k):
        		res[i] = j
        		if res[i] != res[i-1]:
        			self.find_ways(n, k, start, res, allRes)



    def find_ways(self, n, k, start, res, allRes):
    	