class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
    	if n < 0:
    		return 0
    	i = 0
    	while n > 5**i:
    		i += 1
    	total = 0
    	for num in xrange(1,i):
    		total += n / 5 ** num
        return total 

a = Solution()
a.trailingZeros(1000)
