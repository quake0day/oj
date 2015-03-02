class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
    	total = 0
    	for x in xrange(n+1):
    		c = str(x)
    		for char in xrange(len(c)):
    			if c[char] == str(k):
    				total += 1
    	return total

a = Solution()
a.digitCounts(1,12)
